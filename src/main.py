import untis

def main():
    # Generate client 
    client = untis.Client()

    # Create copy of timetable
    timetable = client.getWeeklyCalendar()

    days = []    
    for day in timetable["days"]:
        days.append({
            "date": day["date"],
            "entries": day["gridEntries"]
        })
    
    print(days[0])

if __name__ == "__main__":
    main()