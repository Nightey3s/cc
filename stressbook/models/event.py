from datetime import datetime
from db_connection import events_collection 
                       
sample_events = [{
    "_id": "event_id_001",
    "type": "Concert",
    "name": "Honkai Impact Music Fest 2024",
    "date": "15/12/2024 19:00:00",
    "location": "Singapore Indoor Stadium",
    "available_tickets": 12000,
    "reserved_tickets": 0,
    "sold_tickets": 0,
    "image_url": "static/images/concert_one.jpeg",
    "duration": "2 hours",
    "age_advisory": "PG-13",
    "description": "Experience the magical world of Honkai Impact through an orchestral performance featuring beloved tracks from the game.",
    "synopsis": "Join us for an unforgettable evening of music from Honkai Impact. The concert will feature a full orchestra performing iconic tracks from the game's soundtrack, accompanied by stunning visuals on the big screen. Please note that this event features actresses cosplaying game characters who may wear revealing costumes.",
    "artist": "HOYO-MiX Symphony Orchestra",
    "organizer": "HoYoverse Entertainment",
    "terms_conditions": [
        "No photography or video recording allowed during the performance",
        "Late entry will only be permitted during suitable breaks",
        "No refunds or exchanges permitted",
        "Parental guidance is advised due to cosplay performances featuring revealing costumes"
    ],
    "faq": [
        {
            "question": "Is there a dress code?",
            "answer": "Smart casual is recommended"
        },
        {
            "question": "Are cameras allowed?",
            "answer": "No photography or recording devices are permitted during the show"
        },
        {
            "question": "Will there be cosplayers at the event?",
            "answer": "Yes, professional actresses will be cosplaying game characters. Please note that some costumes may be revealing, as they stay true to the original character designs."
        }
    ],
    "highlights": [
        "Live orchestral performance",
        "HD screen projections", 
        "Exclusive merchandise",
        "Meet & greet opportunities with cosplaying performers"
    ]
},

{
    "_id": "event_id_002",
    "type": "Concert",
    "name": "Genshin Impact Music Fest 2024",
    "date": "2024-12-18T19:00:00Z",
    "location": "Singapore Indoor Stadium",
    "available_tickets": 12000,
    "reserved_tickets": 0,
    "sold_tickets": 0,
    "image_url": "static/images/concert_two.jpeg",
    "duration": "2 hours",
    "age_advisory": "General Audience",
    "description": "Immerse yourself in the enchanting world of Teyvat through a spectacular orchestral concert featuring the beloved music of Genshin Impact.",
    "synopsis": "Experience an extraordinary evening of music from Genshin Impact. The concert will showcase a full orchestra performing the game's most iconic melodies, complemented by stunning game footage and visual effects.",
    "artist": "HOYO-MiX Symphony Orchestra",
    "organizer": "HoYoverse Entertainment",
    "terms_conditions": [
        "No photography or video recording allowed during the performance",
        "Late entry will only be permitted during suitable breaks",
        "No refunds or exchanges permitted"
    ],
    "faq": [
        {
            "question": "Is there a dress code?",
            "answer": "Smart casual is recommended"
        },
        {
            "question": "Are cameras allowed?",
            "answer": "No photography or recording devices are permitted during the show"
        }
    ],
    "highlights": [
        "Live orchestral performance",
        "HD screen projections",
        "Exclusive merchandise",
        "Meet & greet opportunities"
    ]
},
{
    "_id": "event_id_003",
    "type": "Concert", 
    "name": "Honkai Star Rail Music Fest 2024",
    "date": "24/12/2024 19:00:00",
    "location": "Singapore Indoor Stadium",
    "available_tickets": 12000,
    "reserved_tickets": 0,
    "sold_tickets": 0,
    "image_url": "static/images/concert_three.jpeg",
    "duration": "2 hours",
    "age_advisory": "General Audience",
    "description": "Embark on a musical journey through the cosmos with the stellar soundtrack of Honkai: Star Rail performed live in concert.",
    "synopsis": "Join us for a stellar evening of music from Honkai: Star Rail. Experience the cosmic adventure through orchestral arrangements of the game's soundtrack, accompanied by spectacular visuals from your favorite moments.",
    "artist": "HOYO-MiX Symphony Orchestra",
    "organizer": "HoYoverse Entertainment",
    "terms_conditions": [
        "No photography or video recording allowed during the performance",
        "Late entry will only be permitted during suitable breaks",
        "No refunds or exchanges permitted"
    ],
    "faq": [
        {
            "question": "Is there a dress code?",
            "answer": "Smart casual is recommended"
        },
        {
            "question": "Are cameras allowed?",
            "answer": "No photography or recording devices are permitted during the show"
        }
    ],
    "highlights": [
        "Live orchestral performance",
        "HD screen projections",
        "Exclusive merchandise", 
        "Meet & greet opportunities"
    ]
}]

def create_events_onload():
    # Check if events already exist
    if events_collection.count_documents({}) == 0:
        events_collection.insert_many(sample_events)
        print("Sample events inserted into the database.")
    else:
        print("Events already initialized.")

def retrieve_events():
    return list(events_collection.find())

def get_event_by_id(event_id):
    try:
        event = events_collection.find_one({"_id": event_id})
        if not event:
            print(f"No event found with ID: {event_id}")
            return None
        return event
    except Exception as e:
        print(f"Error retrieving event: {str(e)}")
        return None

def reset_events():
    events_collection.delete_many({})
    events_collection.insert_many(sample_events)
    
    # Verify the insertion
    count = events_collection.count_documents({})
    print(f"Database reset with {count} events")
    
    # Print all events to verify
    all_events = list(events_collection.find())
    for event in all_events:
        print(f"Event in DB: {event['_id']}")

def update_ticket_count(event_id, quantity, action="sold"):
    """Update ticket counts atomically for an event."""
    try:
        if action == "sold":
            result = events_collection.update_one(
                {"_id": event_id, "available_tickets": {"$gte": quantity}},
                {
                    "$inc": {
                        "available_tickets": -quantity,
                        "sold_tickets": quantity
                    }
                }
            )
        elif action == "refund":
            result = events_collection.update_one(
                {"_id": event_id},
                {
                    "$inc": {
                        "available_tickets": quantity,
                        "sold_tickets": -quantity
                    }
                }
            )
        return result.modified_count > 0
    except Exception as e:
        print(f"Error updating ticket count: {str(e)}")
        return False


def check_ticket_availability(event_id, quantity):
    """Check if enough tickets are available"""
    try:
        event = events_collection.find_one({"_id": event_id})
        if not event:
            return False
        return event.get('available_tickets', 0) >= quantity
    except Exception as e:
        print(f"Error checking ticket availability: {str(e)}")
        return False
