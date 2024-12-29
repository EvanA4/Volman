from datetime import datetime, timedelta
from django.utils import timezone
from display.models import Session, Volunteer
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
import names


NUM_VOLS = 50
NUM_SESSIONS = 50
MAX_SESSIONS_PER_VOL = 3
OLDEST_CREATEDAT = timezone.make_aware(datetime(2004, 4, 16, 0, 0, 0))
YOUNGEST_AGE = 15
WORK_CHANCE = .5


def random_time(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(seconds=random.random() * delta.total_seconds())


def vol_init(vols: list[Volunteer]):
    namesset = set[str]([])

    # get list of volunteers
    for id in range(NUM_VOLS):
        newvol = Volunteer()
        newvol.age = random.randint(YOUNGEST_AGE, 75)

        # get a new name
        newvol.name = names.get_full_name()
        while newvol.name in namesset:
            newvol.name = names.get_full_name()
        namesset.add(newvol.name)

        # use name for email
        newvol.email = newvol.name.replace(" ", "").lower() + "@example.com"

        # get time of creation (must be after the person turned YOUNGEST_AGE)
        agethresh = timezone.now() - timedelta(days=(newvol.age - YOUNGEST_AGE) * 365)
        newvol.createdAt = random_time(agethresh if OLDEST_CREATEDAT < agethresh else OLDEST_CREATEDAT, timezone.now())

        newvol.save()
        vols.append(newvol)


def seshs_init(seshs: list[Session]):
    # get list of volunteers
    for id in range(NUM_VOLS):
        newsesh = Session()
        newsesh.beganAt = random_time(OLDEST_CREATEDAT, timezone.now())
        newsesh.length = random.randint(1, 16) / 2

        newsesh.save()
        seshs.append(newsesh)


def connect(vols: list[Volunteer], seshs: list[Session]):
    for vol in vols:
        # for each vol, iterate through all sessions
        for sesh in seshs:
            # if session is AFTER time vol was created, flip coin to see if vol worked there
            if sesh.beganAt > vol.createdAt:
                if random.random() < WORK_CHANCE:
                    # if so, add pk to sessions array
                    vol.sessions.add(sesh.pk)


def add_users(vols: list[Volunteer]):
    # add admin superuser
    User.objects.create_superuser('admin', 'admin@example.com', 'password')

    # add other volunteers as regular users
    for vol in vols:
        newuser = User()
        newuser.username = f"u_{vol.name.replace(" ", "").lower()}"
        newuser.set_password("userpass")
        newuser.email = vol.email
        newuser.first_name = vol.name.split(" ")[0]
        newuser.last_name = vol.name.split(" ")[1]
        newuser.save()


class Command(BaseCommand):
    help = "Create the volunteers, sessions, their relations, and the users for authorization"

    def handle(self, *args, **kwargs):
        # delete pre-existing data
        print("Deleting all volunteers, sessions, and users...")
        Volunteer.objects.all().delete()
        Session.objects.all().delete()
        User.objects.all().delete()

        # create volunteers and sessions
        print("Creating volunteers...")
        vols: list[Volunteer] = []
        vol_init(vols)

        print("Creating sessions...")
        seshs: list[Session] = []
        seshs_init(seshs)

        connect(vols, seshs)

        # add volunteers as users for authentication
        print("Creating users...")
        add_users(vols)