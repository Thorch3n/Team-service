from django.test import TestCase
from .models import Team

class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Team Alpha")

    def test_team_creation(self):
        """Тест создания команды"""
        team = Team.objects.get(name="Team Alpha")
        self.assertEqual(team.name, "Team Alpha")

    def test_team_update(self):
        """Тест обновления состава команды"""
        team = Team.objects.get(name="Team Alpha")
        team.members = ["Alice", "Bob"]
        team.save()
        self.assertEqual(team.members, ["Alice", "Bob"])

    def test_team_deletion(self):
        """Тест удаления команды"""
        team = Team.objects.get(name="Team Alpha")
        team.delete()
        self.assertEqual(Team.objects.count(), 0)
