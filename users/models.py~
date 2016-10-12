from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _

# the User model captures {{username, password, email, first_name, last_name}}


class Writer(models.Model):
    COUNTRIES = (
        ('AD', 'Andorra'),
        ('AE', 'United Arab Emirates'),
        ('AF', 'Afghanistan'),
        ('AG', 'Antigua & Barbuda'),
        ('AI', 'Anguilla'),
        ('AL', 'Albania'),
        ('AM', 'Armenia'),
        ('AN', 'Netherlands Antilles'),
        ('AO', 'Angola'),
        ('AQ', 'Antarctica'),
        ('AR', 'Argentina'),
        ('AS', 'American Samoa'),
        ('AT', 'Austria'),
        ('AU', 'Australia'),
        ('AW', 'Aruba'),
        ('AZ', 'Azerbaijan'),
        ('BA', 'Bosnia and Herzegovina'),
        ('BB', 'Barbados'),
        ('BD', 'Bangladesh'),
        ('BE', 'Belgium'),
        ('BF', 'Burkina Faso'),
        ('BG', 'Bulgaria'),
        ('BH', 'Bahrain'),
        ('BI', 'Burundi'),
        ('BJ', 'Benin'),
        ('BM', 'Bermuda'),
        ('BN', 'Brunei Darussalam'),
        ('BO', 'Bolivia'),
        ('BR', 'Brazil'),
        ('BS', 'Bahama'),
        ('BT', 'Bhutan'),
        ('BV', 'Bouvet Island'),
        ('BW', 'Botswana'),
        ('BY', 'Belarus'),
        ('BZ', 'Belize'),
        ('CA', 'Canada'),
        ('CC', 'Cocos (Keeling) Islands'),
        ('CF', 'Central African Republic'),
        ('CG', 'Congo'),
        ('CH', 'Switzerland'),
        ('CI', 'Ivory Coast'),
        ('CK', 'Cook Iislands'),
        ('CL', 'Chile'),
        ('CM', 'Cameroon'),
        ('CN', 'China'),
        ('CO', 'Colombia'),
        ('CR', 'Costa Rica'),
        ('CU', 'Cuba'),
        ('CV', 'Cape Verde'),
        ('CX', 'Christmas Island'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('DE', 'Germany'),
        ('DJ', 'Djibouti'),
        ('DK', 'Denmark'),
        ('DM', 'Dominica'),
        ('DO', 'Dominican Republic'),
        ('DZ', 'Algeria'),
        ('EC', 'Ecuador'),
        ('EE', 'Estonia'),
        ('EG', 'Egypt'),
        ('EH', 'Western Sahara'),
        ('ER', 'Eritrea'),
        ('ES', 'Spain'),
        ('ET', 'Ethiopia'),
        ('FI', 'Finland'),
        ('FJ', 'Fiji'),
        ('FK', 'Falkland Islands (Malvinas)'),
        ('FM', 'Micronesia'),
        ('FO', 'Faroe Islands'),
        ('FR', 'France'),
        ('FX', 'France, Metropolitan'),
        ('GA', 'Gabon'),
        ('GB', 'United Kingdom (Great Britain)'),
        ('GD', 'Grenada'),
        ('GE', 'Georgia'),
        ('GF', 'French Guiana'),
        ('GH', 'Ghana'),
        ('GI', 'Gibraltar'),
        ('GL', 'Greenland'),
        ('GM', 'Gambia'),
        ('GN', 'Guinea'),
        ('GP', 'Guadeloupe'),
        ('GQ', 'Equatorial Guinea'),
        ('GR', 'Greece'),
        ('GS', 'South Georgia and the South Sandwich Islands'),
        ('GT', 'Guatemala'),
        ('GU', 'Guam'),
        ('GW', 'Guinea-Bissau'),
        ('GY', 'Guyana'),
        ('HK', 'Hong Kong'),
        ('HM', 'Heard & McDonald Islands'),
        ('HN', 'Honduras'),
        ('HR', 'Croatia'),
        ('HT', 'Haiti'),
        ('HU', 'Hungary'),
        ('ID', 'Indonesia'),
        ('IE', 'Ireland'),
        ('IL', 'Israel'),
        ('IN', 'India'),
        ('IO', 'British Indian Ocean Territory'),
        ('IQ', 'Iraq'),
        ('IR', 'Islamic Republic of Iran'),
        ('IS', 'Iceland'),
        ('IT', 'Italy'),
        ('JM', 'Jamaica'),
        ('JO', 'Jordan'),
        ('JP', 'Japan'),
        ('KE', 'Kenya'),
        ('KG', 'Kyrgyzstan'),
        ('KH', 'Cambodia'),
        ('KI', 'Kiribati'),
        ('KM', 'Comoros'),
        ('KN', 'St. Kitts and Nevis'),
        ('KP', 'Korea, Democratic People\'s Republic of'),
        ('KR', 'Korea, Republic of'),
        ('KW', 'Kuwait'),
        ('KY', 'Cayman Islands'),
        ('KZ', 'Kazakhstan'),
        ('LA', 'Lao People\'s Democratic Republic'),
        ('LB', 'Lebanon'),
        ('LC', 'Saint Lucia'),
        ('LI', 'Liechtenstein'),
        ('LK', 'Sri Lanka'),
        ('LR', 'Liberia'),
        ('LS', 'Lesotho'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('LV', 'Latvia'),
        ('LY', 'Libyan Arab Jamahiriya'),
        ('MA', 'Morocco'),
        ('MC', 'Monaco'),
        ('MD', 'Moldova, Republic of'),
        ('MG', 'Madagascar'),
        ('MH', 'Marshall Islands'),
        ('ML', 'Mali'),
        ('MN', 'Mongolia'),
        ('MM', 'Myanmar'),
        ('MO', 'Macau'),
        ('MP', 'Northern Mariana Islands'),
        ('MQ', 'Martinique'),
        ('MR', 'Mauritania'),
        ('MS', 'Monserrat'),
        ('MT', 'Malta'),
        ('MU', 'Mauritius'),
        ('MV', 'Maldives'),
        ('MW', 'Malawi'),
        ('MX', 'Mexico'),
        ('MY', 'Malaysia'),
        ('MZ', 'Mozambique'),
        ('NA', 'Namibia'),
        ('NC', 'New Caledonia'),
        ('NE', 'Niger'),
        ('NF', 'Norfolk Island'),
        ('NG', 'Nigeria'),
        ('NI', 'Nicaragua'),
        ('NL', 'Netherlands'),
        ('NO', 'Norway'),
        ('NP', 'Nepal'),
        ('NR', 'Nauru'),
        ('NU', 'Niue'),
        ('NZ', 'New Zealand'),
        ('OM', 'Oman'),
        ('PA', 'Panama'),
        ('PE', 'Peru'),
        ('PF', 'French Polynesia'),
        ('PG', 'Papua New Guinea'),
        ('PH', 'Philippines'),
        ('PK', 'Pakistan'),
        ('PL', 'Poland'),
        ('PM', 'St. Pierre & Miquelon'),
        ('PN', 'Pitcairn'),
        ('PR', 'Puerto Rico'),
        ('PT', 'Portugal'),
        ('PW', 'Palau'),
        ('PY', 'Paraguay'),
        ('QA', 'Qatar'),
        ('RE', 'Reunion'),
        ('RO', 'Romania'),
        ('RU', 'Russian Federation'),
        ('RW', 'Rwanda'),
        ('SA', 'Saudi Arabia'),
        ('SB', 'Solomon Islands'),
        ('SC', 'Seychelles'),
        ('SD', 'Sudan'),
        ('SE', 'Sweden'),
        ('SG', 'Singapore'),
        ('SH', 'St. Helena'),
        ('SI', 'Slovenia'),
        ('SJ', 'Svalbard & Jan Mayen Islands'),
        ('SK', 'Slovakia'),
        ('SL', 'Sierra Leone'),
        ('SM', 'San Marino'),
        ('SN', 'Senegal'),
        ('SO', 'Somalia'),
        ('SR', 'Suriname'),
        ('ST', 'Sao Tome & Principe'),
        ('SV', 'El Salvador'),
        ('SY', 'Syrian Arab Republic'),
        ('SZ', 'Swaziland'),
        ('TC', 'Turks & Caicos Islands'),
        ('TD', 'Chad'),
        ('TF', 'French Southern Territories'),
        ('TG', 'Togo'),
        ('TH', 'Thailand'),
        ('TJ', 'Tajikistan'),
        ('TK', 'Tokelau'),
        ('TM', 'Turkmenistan'),
        ('TN', 'Tunisia'),
        ('TO', 'Tonga'),
        ('TP', 'East Timor'),
        ('TR', 'Turkey'),
        ('TT', 'Trinidad & Tobago'),
        ('TV', 'Tuvalu'),
        ('TW', 'Taiwan, Province of China'),
        ('TZ', 'Tanzania, United Republic of'),
        ('UA', 'Ukraine'),
        ('UG', 'Uganda'),
        ('UM', 'United States Minor Outlying Islands'),
        ('US', 'United States of America'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistan'),
        ('VA', 'Vatican City State (Holy See)'),
        ('VC', 'St. Vincent & the Grenadines'),
        ('VE', 'Venezuela'),
        ('VG', 'British Virgin Islands'),
        ('VI', 'United States Virgin Islands'),
        ('VN', 'Viet Nam'),
        ('VU', 'Vanuatu'),
        ('WF', 'Wallis & Futuna Islands'),
        ('WS', 'Samoa'),
        ('YE', 'Yemen'),
        ('YT', 'Mayotte'),
        ('YU', 'Yugoslavia'),
        ('ZA', 'South Africa'),
        ('ZM', 'Zambia'),
        ('ZR', 'Zaire'),
        ('ZW', 'Zimbabwe'),
        ('ZZ', 'Unknown or unspecified country'),
    )    
    CAT_CHOICES = (
        ('starter', 'Starter'),
        ('polished', 'Polished'),
        ('pro', 'Pro'),
        ('master', 'Master'),
    )
    STAT_CHOICES = (
        ('waiting', 'Waiting'),
        ('suspended', 'Suspended'),
        ('active', 'Active'),
        ('closed', 'Closed'),
    )
    GEN_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('neutral','Neutral'),
    )
    LANG_CHOICES = (
        ('english', 'English'),
        ('french', 'French'),
        ('chinese', 'Chinese'),
        ('spanish', 'Spanish'),
        ('hindi', 'Hindi'),
        ('arabic', 'Arabic'),
        ('ukranian', 'Ukranian'),
        ('portuguese', 'Portuguese'),
        ('russian', 'Russian'),
        ('japanese', 'Japanese'),
        ('bengali', 'Bengali'),
        ('german', 'German'),
        ('other', 'Other'),
    )
    
    EDU_CHOICES = (
        ('diploma', 'Diploma'),
        ('bachelor', 'Bachelor'),
        ('masters', 'Masters'),
        ('phd', 'PhD'),
    )
    
    writerid = models.IntegerField()
    user = models.OneToOneField(User)
    category = models.CharField (max_length=10,
    	choices = CAT_CHOICES,
        default = 'starter')
    status = models.CharField (max_length=10,
    	choices = STAT_CHOICES,
        default = 'waiting')
    gender = models.CharField (max_length=10,
    	choices = GEN_CHOICES,
        default = 'neutral')
    notifications = models.BooleanField()
    native_language = models.CharField (max_length=10,
    	choices = LANG_CHOICES,
        default = 'english')
    experience = models.IntegerField()
    ratings = models.IntegerField()
    cum_rating = models.FloatField()
    timezone = models.CharField(max_length=25)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length = 15) # validators should be a list
    skype = models.CharField(max_length=25)
    country = models.CharField (max_length=10,
    	choices = COUNTRIES,
        default = 'ZZ') 
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    education = models.CharField (max_length=10,
    	choices = EDU_CHOICES,
        default = 'diploma')
    warnings = models.SmallIntegerField()
    earned = models.FloatField()
    #jobs = 

class Supaa(Writer):
    SHIFT_CHOICES= (
        ('one', 'One'),
        ('two', 'Two'),
        ('three', 'Three'),
        ('four', 'Four'),
    )
    DEPT_CHOICES= (
        ('all', 'All'),
        ('payment', 'Payment Dpt'),
        ('quality', 'Quality Assurance Dpt.'),
        ('dissertation', 'Dissertation Dpt.'),
        ('writers', 'Writers Dpt.'),
        ('support', 'Support Dpt.'),
        ('customer', 'Customer'),
        ('mentors', 'Mentors Dpt.'),
        ('writersO', 'Writers Offices Dpt.'),
        ('recruiting', 'Recruiting Dpt.'),
        ('editors', 'Editors Dpt.'),
    )
    shift = models.CharField (max_length=10,
    	choices = SHIFT_CHOICES,
        default = 'one')
    department = models.CharField (max_length=10,
    	choices = DEPT_CHOICES,
        default = 'all')


class Affiliate(models.Model):
    affiliateid = models.IntegerField()
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length = 15) # validators should be a list
    #clients = 
    

class Client(models.Model):
    clientid = models.IntegerField()
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list 
    referer = models.OneToOneField(Affiliate, unique=True)
    #jobs = 
    #spent = self.jobs.value....
    #ratings =
    #cum_ratings =  
    balance = models.IntegerField()
    #photo = 
