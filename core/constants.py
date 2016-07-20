

BASE_STATUSES = (
    (0, "Active"),
    (1, "Inactive"),
)
IS_ACTIVE = 0
IS_INACTIVE = 1

JOB_ROLES = (
    ('Artist', 'Artist'),
    ('Assistant', 'Assistant'),
    ('Assistant / Associate Producer', 'Assistant / Associate Producer'),
    ('Brand Agency', 'Brand Agency'),
    ('Brand/Corporate', 'Brand/Corporate'),
    ('Camera', 'Camera'),
    ('Charity', 'Charity'),
    ('Company Director', 'Company Director'),
    ('Company providing film services', 'Company providing film services'),
    ('Director', 'Director'),
    ('Editor', 'Editor'),
    ('Educational', 'Educational'),
    ('Film Organisation', 'Film Organisation'),
    ('Financier', 'Financier'),
    ('Foundation', 'Foundation'),
    ('Gallery', 'Gallery'),
    ('Journalist', 'Journalist'),
    ('Lawyer', 'Lawyer'),
    ('Media - Broadcaster', 'Media - Broadcaster'),
    ('Media - Digital', 'Media - Digital'),
    ('Media - Distributor', 'Media - Distributor'),
    ('Media - Film Festival', 'Media - Film Festival'),
    ('Media - Post Production', 'Media - Post Production'),
    ('Media - Press and PR', 'Media - Press and PR'),
    ('NGO - Comms', 'NGO - Comms'),
    ('NGO - Campaigns', 'NGO - Campaigns'),
    ('Philanthropist', 'Philanthropist'),
    ('Photographer', 'Photographer'),
    ('Politics', 'Politics'),
    ('Producer', 'Producer'),
    ('Production Management', 'Production Management'),
    ('Runner', 'Runner'),
    ('Sales Agent', 'Sales Agent'),
    ('Social Entrepreneur', 'Social Entrepreneur'),
    ('Sound', 'Sound'),
    ('Student', 'Student'),
    ('Writer', 'Writer'),
)

REGIONS = (
    ('England' , 'England'),
    ('Scotland', 'Scotland'),
    ('Wales' , 'Wales'),
    ('Northern Ireland', 'Northern Ireland'),
    ('British Isles' , 'British Isles'),
    ('Channel Islands' , 'Channel Islands'),
    ('Isle of Man' , 'Isle of Man'),
    ('Albania' , 'Albania'),
    ('Armenia' , 'Armenia',),
    ('Austria' , 'Austria',),
    ('Belgium' , 'Belgium',),
    ('Bulgaria', 'Bulgaria'),
    ('Cyprus', 'Cyprus',),
    ('Czech Republic', 'Czech Republic',),
    ('Finland' , 'Finland',),
    ('Denmark' , 'Denmark'),
    ('France', 'France'),
    ('Germany' , 'Germany'),
    ('Greece', 'Greece'),
    ('Iceland' , 'Iceland'),
    ('Ireland' , 'Ireland'),
    ('Italy' , 'Italy'),
    ('Netherlands' , 'Netherlands'),
    ('Norway', 'Norway'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Romania' , 'Romania'),
    ('Serbia', 'Serbia'),
    ('Slovenia', 'Slovenia'),
    ('Slovakia', 'Slovakia'),
    ('Spain' , 'Spain'),
    ('Sweden', 'Sweden'),
    ('Switzerland' , 'Switzerland'),
    ('Turkey', 'Turkey',),
    ('Ukraine' , 'Ukraine',),
    ('Other EU', 'Other EU'  ),
    ('Algeria' , 'Algeria', ),
    ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
    ('Egypt' , 'Egypt'),
    ('Ghana' , 'Ghana', ),
    ('Kenya' , 'Kenya',),
    ('Liberia' , 'Liberia', ),
    ('Malawi', 'Malawi',     ),
    ('Morocco' , 'Morocco',  ),
    ('Nigeria' , 'Nigeria',      ),
    ('Senegal' , 'Senegal',    ),
    ('South Africa', 'South Africa'),
    ('Tanzania', 'Tanzania'),
    ('Tunisia' , 'Tunisia',  ),
    ('Zimbabwe', 'Zimbabwe'),
    ('Other Africa', 'Other Africa'),
    ('Afghanistan' , 'Afghanistan'),
    ('Bangladesh', 'Bangladesh'),
    ('China, People\'s Republic of', 'China, People\'s Republic of'),
    ('India' , 'India'),
    ('Indonesia' , 'Indonesia'),
    ('Iran'  , 'Iran'),
    ('Iraq'  , 'Iraq'),
    ('Israel', 'Israel'),
    ('Palestine' , 'Palestine'),
    ('Japan' , 'Japan'),
    ('Malaysia', 'Malaysia',),
    ('North Korea' , 'North Korea'),
    ('Pakistan', 'Pakistan',),
    ('Philippines' , 'Philippines'),
    ('Russia', 'Russia'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Singapore' , 'Singapore'),
    ('South Korea' , 'South Korea'),
    ('Sri Lanka' , 'Sri Lanka',),
    ('Syria' , 'Syria',),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('Other Asia', 'Other Asia'),
    ('Canada', 'Canada'),
    ('New York City' , 'New York City'),
    ('San Francisco' , 'San Francisco'),
    ('Los Angeles' , 'Los Angeles'),
    ('New York', 'New York'),
    ('Washington DC' , 'Washington DC'),
    ('California', 'California'),
    ('Alabama' , 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona' , 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('Colorado', 'Colorado'),
    ('Connecticut' , 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida' , 'Florida'),
    ('Georgia' , 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho' , 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana' , 'Indiana'),
    ('Iowa'  , 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana' , 'Louisiana'),
    ('Maine' , 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts' , 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota' , 'Minnesota'),
    ('Mississippi' , 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana' , 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire' , 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio'  , 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee' , 'Tennessee'),
    ('Texas' , 'Texas'),
    ('Utah'  , 'Utah'),
    ('Vermont' , 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia' , 'West Virginia'),
    ('Wisconsin' , 'Wisconsin'),
    ('Wyoming ', 'Wyoming' ),
    ('Argentina' , 'Argentina'),
    ('Barbados', 'Barbados'),
    ('Belize', 'Belize',),
    ('Brazil', 'Brazil'),
    ('Chile' , 'Chile'),
    ('Colombia', 'Colombia',),
    ('Cuba'  , 'Cuba',),
    ('Ecuador' , 'Ecuador'),
    ('Haiti' , 'Haiti'),
    ('Honduras', 'Honduras'),
    ('Jamaica' , 'Jamaica'),
    ('Mexico', 'Mexico'),
    ('Peru'  , 'Peru'),
    ('Venezuela' , 'Venezuela'),
    ('Other Central America' , 'Other Central America'),
    ('Other South America' , 'Other South America'),
    ('Other Caribbean' , 'Other Caribbean' ),
    ('New Zealand' , 'New Zealand'),
    ('Australia' , 'Australia'),
    ('Other Oceania' , 'Other Oceania')
)