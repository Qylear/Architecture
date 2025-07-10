# test_enrolement.py

import unittest
from unittest.mock import MagicMock, patch
from config.database import SessionLocal
from models.enrolement import Enrolement
from models.enrolement import Enrolement  # La fonction à tester

class TestGetAllEnrolements(unittest.TestCase):
    @patch('my_app.services.SessionLocal')
    def test_get_all_enrolements_returns_all_items(self, mock_session_local):
        # Préparation
        mock_db = MagicMock()
        mock_session_local.return_value = mock_db
        mock_query = mock_db.query.return_value
        mock_query.all.return_value = ['enrol1', 'enrol2']

        # Exécution
        result = Enrolement.get_all_enrolements()

        # Vérifications
        mock_db.query.assert_called_once_with(Enrolement)
        mock_query.all.assert_called_once()
        mock_db.close.assert_called_once()
        self.assertEqual(result, ['enrol1', 'enrol2'])
