from tabnanny import verbose
from django.db import models
from vehicles.models import Vehicle


class ParkingSpot(models.Model):
    spot_number = models.CharField(max_length=10, verbose_name='Número da vaga', unique=True)
    is_available = models.BooleanField(default=True, verbose_name='Disponível')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vaga de estacionamento'
        verbose_name_plural = 'Vagas de estacionamento'
        
    def __str__(self):
        return self.spot_number
    
class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, 
        on_delete=models.PROTECT, 
        related_name='parking_records', 
        verbose_name='Veículo'
    )
    parking_spot = models.ForeignKey(
        ParkingSpot, 
        on_delete=models.PROTECT, 
        related_name='parking_records', 
        verbose_name='Vaga'
    )
    check_in_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Hora de entrada'
    )
    check_out_time = models.DateTimeField(
        null=True,                                
        blank=True, 
        verbose_name='Hora de saída'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Registro de estacionamento'
        verbose_name_plural = 'Registros de estacionamento'

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot} - {self.check_in_time}'
