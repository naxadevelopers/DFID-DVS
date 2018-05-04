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


class ProgramBudget(models.Model):
    program = models.ForeignKey(Program, related_name="program_budget", on_delete=models.CASCADE)
    code = models.IntegerField()
    budget = models.FloatField(default=0)


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

    def active_programmes(self):
        return self.province.program_data_province.values('id', 'program__name')

    def total_budget(self):
        return self.province.program_data_province.aggregate(total=Sum('program__program_budget__budget'))

    def description(self):
        return self.province.description


class DistrictSpending(models.Model):
    district = models.ForeignKey(District, related_name="district_spending", on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey(Program, related_name="district_spending_program", on_delete=models.SET_NULL, null=True)
    annual_spend = models.FloatField()


class Indicator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FederalismDraft(models.Model):
    dfid_qn = models.IntegerField()
    province = models.ForeignKey(Province, related_name="federalism_draft_province", on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, related_name="federalism_draft_province_indicator",
                                  on_delete=models.SET_NULL, null=True)
    values = models.FloatField()
    unit = models.CharField(max_length=200)


class ProvinceInfo(models.Model):
    name = models.ForeignKey(Province, related_name="province_info", on_delete=models.CASCADE)

    def total_budget(self):
        return self.name.program_data_province.aggregate(total=Sum('program__program_budget__budget'))

    def active_programmes(self):
        return self.name.program_data_province.values('program').count()


class ProgramData(models.Model):
    province = models.ManyToManyField(Province, related_name="program_data_province")
    program = models.ForeignKey(Program, related_name="program_data_program", on_delete=models.CASCADE)

    def program_budget(self):
        try:
            return self.program.program_budget.values_list('budget', flat=True)[0]
        except IndexError:
            pass

    def description(self):
        return self.program.description

    def sectors(self):
        return self.program.sector_data_program.extra(select={'id': 'sector_id'}).values('id', 'sector__name')


class CountryData(models.Model):
    provinces = models.IntegerField(default=7)
    paalikas = models.IntegerField(default=460)
    municipalities = models.IntegerField(default=276)
    total_population = models.IntegerField(default=29624035)
    area = models.CharField(max_length=200, default="147,181 sq.km")
    population_density = models.IntegerField(null=True)
    poverty_rate = models.FloatField(null=True)
    literacy_rate = models.FloatField(null=True)
    population_under_poverty_line = models.IntegerField(null=True)
    per_capita_income = models.IntegerField(null=True)
    human_development_index = models.FloatField(null=True)
    gdp = models.IntegerField(null=True)


class SectorData(models.Model):
    sector = models.ForeignKey(Sector, related_name="sector_data_sector", on_delete=models.CASCADE)
    program = models.ForeignKey(Program, related_name="sector_data_program", on_delete=models.SET_NULL, null=True)
