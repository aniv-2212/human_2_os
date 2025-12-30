import pytest
from app import app
from flask import session

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_key'
    with app.test_client() as client:
        yield client

def test_redirect_to_setup(client):
    """Test that root redirects to setup if no session exists."""
    rv = client.get('/')
    assert rv.status_code == 302
    assert '/setup' in rv.location

def test_setup_submission(client):
    """Test submitting the setup form."""
    rv = client.post('/setup', data={
        'name': 'Test User',
        'skill_neural': '80',
        'skill_systems': '70',
        'skill_ai': '60',
        'skill_strat': '50',
        'interests': 'AI, Code',
        'goals': 'CTO',
        'bio_stress': '30',
        'bio_energy': '80',
        'bio_focus': '90'
    }, follow_redirects=True)
    
    assert rv.status_code == 200
    # The dashboard shows the ID, e.g., dt_test_user
    assert b"dt_test_user" in rv.data
    assert b"Digital Twin Profile" in rv.data

def test_dashboard_access(client):
    """Test accessing dashboard after setup."""
    # First setup
    client.post('/setup', data={
        'name': 'Test User',
        'skill_neural': '50',
        'skill_systems': '50',
        'skill_ai': '50',
        'skill_strat': '50',
        'interests': 'A',
        'goals': 'B',
        'bio_stress': '50',
        'bio_energy': '50',
        'bio_focus': '50'
    }, follow_redirects=True)
    
    # Then access dashboard
    rv = client.get('/dashboard')
    assert rv.status_code == 200
    assert b"Human OS v2.0.27" in rv.data

def test_reset_functionality(client):
    """Test the reset button clears the session."""
    # Setup first
    client.post('/setup', data={'name': 'To Be Deleted'}, follow_redirects=True)
    
    # Reset
    rv = client.get('/reset', follow_redirects=True)
    assert rv.status_code == 200
    assert b"Neural Initialization Protocol" in rv.data  # Back to setup page
