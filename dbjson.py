import json
from datetime import datetime, timedelta
import random
import names


NUM_VOLS = 50
NUM_SESSIONS = 50
MAX_SESSIONS_PER_VOL = 3
OLDEST_CREATEDAT = datetime(2004, 4, 16, 0, 0, 0)
YOUNGEST_AGE = 15
WORK_CHANCE = .5


def random_time(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(seconds=random.random() * delta.total_seconds())


def vol_init(vols: list[dict]):
    namesset = set[str]([])

    # get list of volunteers
    for id in range(NUM_VOLS):
        newvol = {
            "pk": id,
            "model": "display.Volunteer",
            "fields": {
                "name": "",
                "age": random.randint(YOUNGEST_AGE, 75),
                "createdAt": "",
                "sessions": [],
            }
        }

        # get a new name
        newvol["fields"]["name"] = names.get_full_name()
        while newvol["fields"]["name"] in namesset:
            newvol["fields"]["name"] = names.get_full_name()
        namesset.add(newvol["fields"]["name"])

        # get time of creation (must be after the person turned YOUNGEST_AGE)
        agethresh = datetime.now() - timedelta(days=(newvol["fields"]["age"] - YOUNGEST_AGE) * 365)
        newvol["fields"]["createdAt"] = random_time(agethresh if OLDEST_CREATEDAT < agethresh else OLDEST_CREATEDAT, datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

        vols.append(newvol)


def seshs_init(seshs: list[dict]):
    # get list of volunteers
    for id in range(NUM_VOLS):
        newsesh = {
            "pk": id,
            "model": "display.Session",
            "fields": {
                "beganAt": "",
                "length": -1,
            }
        }

        newsesh["pk"] = id
        newsesh["fields"]["beganAt"] = random_time(OLDEST_CREATEDAT, datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        newsesh["fields"]["length"] = random.randint(1, 16) / 2
        seshs.append(newsesh)


def connect(vols: list[dict], seshs: list[dict]):
    for vol in vols:
        volTime = datetime.strptime(vol["fields"]["createdAt"], "%Y-%m-%d %H:%M:%S")
        # for each vol, iterate through all sessions
        for sesh in seshs:
            seshTime = datetime.strptime(sesh["fields"]["beganAt"], "%Y-%m-%d %H:%M:%S")
            # if session is AFTER time vol was created, flip coin to see if vol worked there
            if seshTime > volTime and random.random() < WORK_CHANCE:
                # if so, add pk to sessions array
                vol["fields"]["sessions"].append(sesh["pk"])


def main():
    # create vols array WITHOUT sessions
    vols = []
    vol_init(vols)

    # create sessions WITHOUT vols
    seshs = []
    seshs_init(seshs)

    # connect the two
    connect(vols, seshs)

    # create final list of objects
    objs = []
    for vol in vols: objs.append(vol)
    for sesh in seshs: objs.append(sesh)

    # convert vols array to file
    mystr = json.dumps(objs, indent=4)
    file = open("output.json", "w")
    file.write(mystr)
    file.close()


if __name__ == "__main__":
    main()