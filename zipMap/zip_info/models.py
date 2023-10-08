from django.db import models


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=60, blank=True, null=True)
    province = models.ForeignKey('Province', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'District'


class Jurisdiction(models.Model):
    jurisdiction_id = models.AutoField(primary_key=True)
    jurisdiction_name = models.CharField(max_length=60, blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Jurisdiction'


class Neighborhood(models.Model):
    neighborhood_id = models.AutoField(primary_key=True)
    neighborhood_name = models.CharField(max_length=60, blank=True, null=True)
    village = models.ForeignKey('Village', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Neighborhood'


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Province'


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=400)
    natural_name = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    phone = models.IntegerField(blank=True, null=True)
    recovery_email = models.CharField(max_length=100, blank=True, null=True)
    sec_question = models.CharField(max_length=100, blank=True, null=True)
    zip = models.ForeignKey('ZipCode', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User_profile'


class Village(models.Model):
    village_id = models.AutoField(primary_key=True)
    village_name = models.CharField(max_length=60, blank=True, null=True)
    jurisdiction = models.ForeignKey(Jurisdiction, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Village'


class ZipCode(models.Model):
    zip_id = models.AutoField(primary_key=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    province = models.ForeignKey(Province, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Zip_code'