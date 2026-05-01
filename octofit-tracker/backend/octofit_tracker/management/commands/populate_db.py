from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Eliminar datos existentes
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc),
        ]

        # Crear actividades
        Activity.objects.create(user=users[0], type='run', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='bike', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='swim', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='walk', duration=20, calories=100)

        # Crear workouts
        Workout.objects.create(user=users[0], name='Iron Endurance', description='Rutina avanzada de resistencia')
        Workout.objects.create(user=users[2], name='Bat Strength', description='Rutina de fuerza extrema')

        # Crear leaderboard
        Leaderboard.objects.create(user=users[0], points=1000)
        Leaderboard.objects.create(user=users[1], points=800)
        Leaderboard.objects.create(user=users[2], points=950)
        Leaderboard.objects.create(user=users[3], points=900)

        self.stdout.write(self.style.SUCCESS('octofit_db poblada con datos de prueba'))
