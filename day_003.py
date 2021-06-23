"""
Day 3 Project: Treasure Island

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""

print("""
            Treasure Island
            ---------------
            You set off on an adventure to find treasure.""")
while True:
    direction = input("""
            You come to a crossroads. You can go [left] or [right]
            : """).lower()
    if direction == "right":
        print("""
            You come across a wandering gang of rabid weasels.
            When they see you, they immediately attack!
            You are left to die on the pathway...
            
            Game Over.
            """)
        break
    elif direction == "left":
        direction = input("""
            You head down the left path, and soon come across a boat dock.
            You can see an island close by.
            Will you [wait] for the boat, or [swim] across?
            : """).lower()
        if direction == "swim":
            print("""
            After several minutes of swimming, you are surrounded by man-eating piranhas.
            You scream as they begin biting chunks out of you.
            
            Game Over.
            """)
            break
        elif direction == "wait":
            direction = input("""
            A boat arrives after several minutes and offers you a ride
            across to the island. Once there, you notice three doors.
            Will you open the [red], [yellow], or [blue] door?
            : """).lower()
            if direction == "red":
                print("""
            You see a dusty chest across the room.
            You don't see the tripwire until too late.
            Jets of flame shoot from every direction!
            
            Game Over.
                """)
                break
            elif direction == "blue":
                print("""
            Upon entering the room, the door is slammed shut behind you.
            Poisonous gasses begin to fill the room!
            
            Game Over.
                """)
                break
            elif direction == "yellow":
                print("""
            You see a treasure chest overflowing with gold and gems!
            You take as much as you can with you and live happily ever after.
            
            You Win!
                """)
                break



