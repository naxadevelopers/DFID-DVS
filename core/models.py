from django.db import models
from django.db.models import Sum


class Province(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    @property
    def annual_spend(self):
        return self.districts.aggregate(total=Sum('district_spending__annual_spend'))

    @property
    def programs(self):
        return self.districts.values('district_spending__program').distinct().count()

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    province = models.ForeignKey(Province, related_name="districts", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


class Partner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)


class ProvinceData(models.Model):
    province = models.ForeignKey(Province, related_name="province_data", on_delete=models.CASCADE)
    total_population = models.IntegerField()
    area = models.FloatField()
    population_density = models.IntegerField()
    poverty_rate = models.FloatField()
    population_under_poverty_line = models.IntegerField()
    per_capita_income = models.IntegerField()
    hh_by_lowest_wealth_quantiles = models.FloatField()
    human_development_index = models.FloatField()
    minute_access_to = models.FloatField()
    vulnerability_index = models.FloatField()
    gdp = models.IntegerField()


class DistrictSpending(models.Model):
    district = models.ForeignKey(District, related_name="district_spending", on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey(Program, related_name="district_spending_program", on_delete=models.SET_NULL, null=True)
    annual_spend = models.FloatField()