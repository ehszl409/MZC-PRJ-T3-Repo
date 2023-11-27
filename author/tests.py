from django.test import TestCase
from django.contrib.auth.models import User
from .models import AuthorProfile


class AuthorProfileTestCase(TestCase):
    def setUp(self):
        # 테스트를 위한 데이터를 설정합니다.
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.author_profile = AuthorProfile.objects.create(
            user=self.user,
            name="Test Author",
            email="test@example.com",
            about="Test about text",
            photo="path/to/test/photo.jpg",
            gender="male",
            website="http://www.example.com",
            facebook="http://www.facebook.com/testuser",
            twitter="http://www.twitter.com/testuser",
            linkedin="http://www.linkedin.com/in/testuser",
        )

    def test_author_profile_creation(self):
        # AuthorProfile 모델이 정상적으로 생성되는지 테스트합니다.
        self.assertEqual(self.author_profile.user, self.user)
        self.assertEqual(self.author_profile.name, "Test Author")
        self.assertEqual(self.author_profile.email, "test@example.com")
        self.assertEqual(self.author_profile.about, "Test about text")
        self.assertEqual(self.author_profile.photo, "path/to/test/photo.jpg")
        self.assertEqual(self.author_profile.gender, "male")
        self.assertEqual(self.author_profile.website, "http://www.example.com")
        self.assertEqual(
            self.author_profile.facebook, "http://www.facebook.com/testuser"
        )
        self.assertEqual(self.author_profile.twitter, "http://www.twitter.com/testuser")
        self.assertEqual(
            self.author_profile.linkedin, "http://www.linkedin.com/in/testuser"
        )
        self.assertIsNotNone(self.author_profile.date)  # date 필드가 비어있지 않은지 확인
