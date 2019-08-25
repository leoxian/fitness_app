
##部位
class Regions(db.Model):
    __tablename__ = 'region'
    id = db.Column('id',db.Integer,primary_key=True)
    name =db.Column('name',db.String(32))

    def __repr__(self):
        return '<Regin %r>'%self.name

##动作

class action(db.Model):
    __tablename__ ='action'
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name',db.String(32))
    regoin_id =db.Column('regoin_id',db.Integer)

    def __repr__(self):
        return '<action %r>'%self.name


##记录
class record(db.Model):
    __tablename__ ='action'
    id = db.Column('id',db.Integer,primary_key=True)
    plan_time=db.Column('plan_time',db.String(32))
    act_time=db.Column('act_time',db.String(32))
    action_id=db.Column('action_id',db.Integer)
    quantity=db.Column('quantity',db.String(32))
    weight=db.Column('weight',db.Integer)

    def __repr__(self):
        return '<record %r>'%self.name
