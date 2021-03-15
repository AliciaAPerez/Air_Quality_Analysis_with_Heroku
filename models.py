
def create_classes(db):
    class Sites(db.Model):
        __tablename__ = 'Sites'

        site_no = db.Column(db.String(20), primary_key=True)
        CBSA_Name = db.Column(db.String(100))
        Latitude = db.Column(db.Float)
        Longitude = db.Column(db.Float)

        def __repr__(self):
            return '<Sites %r>' % (self.CBSA_Name)
    print(Sites)
    return Sites

    
