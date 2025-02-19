from datetime import datetime
from db_connection import seats_collection , events_collection

# Predefined seat sections with their configurations
seat_sections = [
    {"section": "333", "price": 200, "color": "Periwinkle Blue", "color_code": "#9391f7", "capacity_limit": 200},
    {"section": "332", "price": 200, "color": "Periwinkle Blue", "color_code": "#9391f7", "capacity_limit": 200},
    {"section": "309", "price": 200, "color": "Periwinkle Blue", "color_code": "#9391f7", "capacity_limit": 200},

    {"section": "331", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "330", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "329", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "328", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "327", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "326", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "325", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "324", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "323", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "322", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "320", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "319", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "318", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "314", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "313", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "312", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "311", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},
    {"section": "310", "price": 300, "color": "Lavender Blue", "color_code": "#c9c7fb", "capacity_limit": 100},

    {"section": "233", "price": 300, "color": "Sour Candy", "color_code": "#5bb343", "capacity_limit": 100},
    {"section": "232", "price": 300, "color": "Sour Candy", "color_code": "#5bb343", "capacity_limit": 100},
    {"section": "230", "price": 300, "color": "Sour Candy", "color_code": "#5bb343", "capacity_limit": 100},
    {"section": "229", "price": 300, "color": "Sour Candy", "color_code": "#5bb343", "capacity_limit": 100},
    {"section": "213", "price": 300, "color": "Sour Candy", "color_code": "#5bb343", "capacity_limit": 100},
    {"section": "212", "price": 300, "color": "Sour Candy", "color_code": "#5bb343", "capacity_limit": 150},
    {"section": "209", "price": 300, "color": "Sour Candy", "color_code": "#5bb343", "capacity_limit": 150},
    
    {"section": "231", "price": 300, "color": "Green Gooseberry", "color_code": "#add9a1", "capacity_limit": 150},
    {"section": "210", "price": 300, "color": "Green Gooseberry", "color_code": "#add9a1", "capacity_limit": 150},
    {"section": "211", "price": 300, "color": "Green Gooseberry", "color_code": "#add9a1", "capacity_limit": 150},
    {"section": "114", "price": 300, "color": "Green Gooseberry", "color_code": "#add9a1", "capacity_limit": 150},
    {"section": "219", "price": 300, "color": "Green Gooseberry", "color_code": "#add9a1", "capacity_limit": 150},
    {"section": "223", "price": 300, "color": "Green Gooseberry", "color_code": "#add9a1", "capacity_limit": 150},
    {"section": "128", "price": 300, "color": "Green Gooseberry", "color_code": "#add9a1", "capacity_limit": 150},
    
    {"section": "133", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "132", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "131", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "130", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "129", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "113", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "112", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "111", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "110", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "109", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "222", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "221", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
    {"section": "220", "price": 300, "color": "Peaches N Cream", "color_code": "#f3a7a7", "capacity_limit": 150},
   
    {"section": "228", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "227", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "226", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "225", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "224", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "218", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "217", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "216", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "215", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},
    {"section": "214", "price": 300, "color": "Skullcrusher Brass", "color_code": "#efc58f", "capacity_limit": 200},

    {"section": "pa2", "price": 400, "color": "Light Whimsy", "color_code": "#97cfe9", "capacity_limit": 400},
    {"section": "pb2", "price": 400, "color": "Light Whimsy", "color_code": "#97cfe9", "capacity_limit": 400},

    {"section": "234", "price": 300, "color": "Peppermint Frosting", "color_code": "#b3f7ed", "capacity_limit": 200},
    {"section": "208", "price": 300, "color": "Peppermint Frosting", "color_code": "#b3f7ed", "capacity_limit": 200},
    
    {"section": "pa1", "price": 500, "color": "Leaf Bud", "color_code": "#f1ef9d", "capacity_limit": 1000},
    {"section": "pb1", "price": 450, "color": "Leaf Bud", "color_code": "#f1ef9d", "capacity_limit": 1000},

    {"section": "134", "price": 500, "color": "Lime Sherbet", "color_code": "#d1d989", "capacity_limit": 200},
    {"section": "108", "price": 450, "color": "Lime Sherbet", "color_code": "#d1d989", "capacity_limit": 200},
]

def initialize_seat_sections():
    events = list(events_collection.find())
    
    for event in events:
        event_id = event["_id"]
        
        # Check if any seat exists for this event
        if seats_collection.count_documents({"event_id": event_id}) > 0:
            print(f"Seats already initialized for event {event_id}, skipping.")
            continue
        
        # Only proceed with insertion if no seats exist for this event
        seats = []
        for section in seat_sections:
            seat_section_id = f"seat_section_{event_id}_{section['section']}"
            seat_section = {
                "_id": seat_section_id,
                "event_id": event_id,
                "section": section["section"],
                "description": f"{section['section']} section in event {event_id}",
                "price": section["price"],
                "available_tickets": section["capacity_limit"],
                "reserved_tickets": 0,
                "sold_tickets": 0,
                "color": section["color"],
                "color_code": section["color_code"],
                "capacity_limit": section["capacity_limit"]
            }
            seats.append(seat_section)
        
        seats_collection.insert_many(seats)
        print(f"Inserted {len(seats)} seat sections for event {event_id}.")

def update_seat_count(event_id, section, quantity):
    """Update seat availability atomically."""
    try:
        result = seats_collection.update_one(
            {"_id": f"seat_section_{event_id}_{section}", "available_tickets": {"$gte": quantity}},
            {
                "$inc": {
                    "available_tickets": -quantity,
                    "reserved_tickets": quantity
                }
            }
        )
        return result.modified_count > 0
    except Exception as e:
        print(f"Error updating seat count: {str(e)}")
        return False

