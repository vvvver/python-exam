from app.app import create_app
from app.models import db
from app.create_db import seed
import os
app = create_app()

with app.app_context():
    db.create_all()
    seed()
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
