from django.db import models


class VehicleType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome", unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Tipo de Veículo"
        verbose_name_plural = "Tipos de Veículos"

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="vehicles",
        verbose_name="Tipo de Veículo",
    )
    owner = models.ForeignKey(
        "customers.Customer",
        on_delete=models.PROTECT,
        related_name="vehicles",
        verbose_name="Proprietário",
        blank=True,
        null=True,
    )
    brand = models.CharField(
        max_length=50,
        verbose_name="Marca",
        blank=True,
        null=True,
    )
    model = models.CharField(
        max_length=50,
        verbose_name="Modelo",
        blank=True,
        null=True,
    )
    plate = models.CharField(max_length=10, unique=True, verbose_name="Placa")
    color = models.CharField(max_length=20, blank=True, null=True, verbose_name="Cor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.plate}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
