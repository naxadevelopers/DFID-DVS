from django.db import models
from django.db.models import Sum, Count


class Province(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    @property
    def annual_spend(self):
        return self.districts.aggregate(total=Sum('district_spending__annual_spend'))

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    province = models.ForeignKey(Province, related_name="districts", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)


class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProgramBudget(models.Model):
    program = models.ForeignKey(Program, related_name="program_budget", on_delete=models.CASCADE)
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

    def district(self):
        return self.province.districts.select_related().count()

    def active_programmes(self):
        return self.province.program_data_province.values(programID=models.F('program'),
                                                          programName=models.F('program__name'))

        # programmes = self.province.program_data_province.all()
        # return [[a.program,a.program__name] for a in programmes]

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
    source = models.CharField(max_length=250, null=True)
    glossary = models.TextField(null=True)

    def __str__(self):
        return self.name


class IndicatorData(models.Model):
    province = models.ForeignKey(Province, related_name="indicator_data_province", on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, related_name="indicator_data_province_indicator",
                                  on_delete=models.SET_NULL, null=True)
    value = models.FloatField()
    unit = models.CharField(max_length=200)
    years = models.IntegerField()
    source = models.CharField(max_length=250)


class ProvinceInfo(models.Model):
    name = models.ForeignKey(Province, related_name="province_info", on_delete=models.CASCADE)
    total_budget = models.FloatField(null=True)

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
        return self.program.sector_data_program.values(sectorId=models.F('sector_id'),
                                                       sectorName=models.F('sector__name'))

    def partners(self):
        return self.partner_program.values('name')

    def total_no_of_partners(self):
        return self.partner_program.count()


class Partner(models.Model):
    name = models.CharField(max_length=200)
    program = models.ForeignKey(ProgramData, on_delete=models.CASCADE, null=True, related_name="partner_program")
    description = models.TextField(null=True, blank=True)


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


class Layer(models.Model):
    name = models.CharField(max_length=250)
    sector = models.ManyToManyField(Sector, related_name="layer")

    def __str__(self):
        return self.name


class LayerData(models.Model):
    layer_name = models.ForeignKey(Layer, related_name='layer_data', on_delete=models.CASCADE)
    source = models.CharField(max_length=250)
    date = models.CharField(max_length=200)
    type = models.CharField(max_length=250)
    notes = models.TextField()
    file = models.FileField(upload_to='layer/', null=True, blank=True)
    layer_server_url = models.CharField(max_length=300, null=True)
    layer_path = models.CharField(max_length=300, null=True)

    def sectors(self):
        sectors = self.layer_name.sector.all()
        return [{'code': sector.code} for sector in sectors]


class Dataset(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    source = models.TextField()
    date = models.DateField()
    url = models.URLField()


class Area(models.Model):
    hlcit_code = models.CharField(max_length=300, unique=True)
    type = models.CharField(max_length=300)
    local_name = models.CharField(max_length=300)
    programs = models.ManyToManyField(ProgramData, blank=True)

    def total_program_budget(self):
        return self.programs.aggregate(total=Sum('program__program_budget__budget'))

    def total_no_of_programmes(self):
        return self.programs.count()


class GlossaryData(models.Model):
    title = models.ForeignKey(Indicator, on_delete=models.CASCADE)
