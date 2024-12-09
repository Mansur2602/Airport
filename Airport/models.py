from django.db import models

# Create your models here.

'''
Airports  - Аэропорты (ID, название) 
Planes    - Самолеты (ID, модель, вместимость, дальность полета, расход топлива и др.) 
Travelers - Пассажиры (ID, ФИО пассажира, возраст и др.) 
Flights   - Фактические рейсы (аэропорт вылета,
            аэропорт назначения, пассажиры, 
            фактическое время вылета-прилета,
            расход топлива и т.д.) 
'''

class Airports( models.Model ):
    # id - BigSerial
    name = models.CharField( max_length = 20, null=False )
    code = models.CharField( max_length = 3, unique=True, null=False, db_index=True  )

    def __str__(self): # 'Astata Airport (NQZ)'
        return f'{self.name} ({self.code})'

    class Meta:
        ordering = [ 'name' ]

class Planes( models.Model ):
    model = models.CharField( max_length = 30, null=False)
    capacity = models.IntegerField()
    distance = models.FloatField()
    consumtion = models.FloatField()
    class Meta:
        pass

class Travels( models.Model ):
    fio = models.CharField(max_length=50, null=False, verbose_name='ФИО парссажира')
    birth_date = models.DateField(null=False, auto_now=False, verbose_name='Дата рождения' )
    passport = models.CharField(max_length=12,
    null=False, unique=True, verbose_name='Документ')
    
    def __str__(self):
        return self.fio
    class Meta:
        ordering = ['fio', '-birth_date']

class Fligth( models.Model ):
    source = models.ForeignKey( Airports, verbose_name='Аэропорт вылета', related_name='rel_source', on_delete=models.CASCADE )
    destination = models.ForeignKey( Airports, related_name='rel_dest', verbose_name='Аэропорт прилета', on_delete=models.CASCADE )
    traveler = models.ForeignKey( Travels, verbose_name='Пассажир', on_delete=models.DO_NOTHING )
    date_depart = models.DateTimeField( auto_now=True, verbose_name='Дата и время вылета' )
    date_arrive = models.DateTimeField( auto_now=False, verbose_name='Дата и время прилета' )
    
    

