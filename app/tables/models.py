from app.tables import db
from app.tables import ma
from datetime import datetime

class Born(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_bayi = db.Column(db.String(100))
    tempat_lahir =  db.Column(db.String(100))
    tanggal_lahir = db.Column(db.String(100))
    jam_lahir = db.Column(db.String(100))
    berat_badan = db.Column(db.String(100))
    jenis_kelamin = db.Column(db.String(100))
    nama_ayah = db.Column(db.String(100))
    nama_ibu = db.Column(db.String(100))
    alamat = db.Column(db.String(100))
    pelapor = db.Column(db.String(100))
    hubungan = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
    
    def update(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def __serialize__(self):
        return {
            'id' : self.id,
            'nama_bayi' : self.nama_bayi,
            'tempat_lahir' : self.tempat_lahir,
            'tanggal_lahir' : self.tanggal_lahir,
            'jam_lahir' : self.jam_lahir,
            'berat_badan' : self.berat_badan,
            'jenis_kelamin' : self.jenis_kelamin,
            'nama_ayah' : self.nama_ayah,
            'nama_ibu' : self.nama_ibu,
            'alamat' : self.alamat,
            'pelapor' : self.pelapor,
            'hubungan' : self.hubungan,
            'created_at' : self.created_at,
            'modified_at' : self.modified_at
        }

db.create_all()

class BornSchema(ma.Schema):
    class Meta:
        model = Born
        fields = [
                    'id', 'nama_bayi', 'tempat_lahir', 'jam_lahir',
                    'berat_badan', 'jenis_kelamin', 'nama_ayah', 'nama_ibu', 
                    'alamat', 'pelapor', 'hubungan', 'created_at', 'modified_at'
        ]

born_schema = BornSchema(many=True) 
    