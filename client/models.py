from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q


def user_image(instance, filename):
    return "%s/%s/%s" % ('profile', instance.username, filename)


class User(AbstractUser):
    cellphone = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    # cellphone_verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.username = self.cellphone
        super(User, self).save(*args, **kwargs)

    def authorize_cellphone(self):
        self.cellphone_verified = True
        self.save()

    @classmethod
    def user_exists(cls, cellphone: str, email: str = None):
        """
        return 'True' if user with 'cellphone' or 'email' is exists.
        """
        if email:
            return cls.objects.filter(Q(cellphone=cellphone) | Q(username=cellphone) | Q(email=email)).exists()
        return cls.objects.filter(Q(cellphone=cellphone) | Q(username=cellphone)).exists()

    @classmethod
    def get_user(cls, cellphone: str, email: str = None):
        """
        return the user with 'cellphone' or 'email'.
        """
        if email:
            return cls.objects.filter(Q(cellphone=cellphone) | Q(username=cellphone) | Q(email=email)).first()
        return cls.objects.filter(Q(cellphone=cellphone) | Q(username=cellphone)).first()

    @staticmethod
    def check_cellphone(cellphone: str):
        if cellphone.startswith("00"):
            cellphone = cellphone.replace("00", "+", 1)
        if cellphone.startswith("0"):
            cellphone = cellphone.replace("0", "", 1)

        prev_numbers = [
            '+93', '+355', '+213', '+1684', '+376', '+244', '+1264', '+1268', '+54', '+374', '+297',
            '+61', '+43', '+994', '+1242', '+973', '+880', '+1246', '+375', '+32', '+501', '+229',
            '+1441', '+975', '+591', '+599', '+387', '+267', '+55', '+1284', '+673', '+359', '+226',
            '+257', '+855', '+237', '+1', '+238', '+1345', '+236', '+235', '+56', '+86', '+57', '+269',
            '+243', '+242', '+682', '+506', '+225', '+385', '+53', '+599', '+357', '+420', '+45', '+246',
            '+253', '+1767', '+1809', '+1829', '+1849', '+593', '+20', '+503', '+240', '+291', '+372',
            '+268', '+251', '+500', '+298', '+679', '+358', '+33', '+594', '+689', '+241', '+220', '+995',
            '+49', '+233', '+350', '+30', '+299', '+1473', '+590', '+1671', '+502', '+224', '+245',
            '+592', '+509', '+504', '+852', '+36', '+354', '+91', '+62', '+98', '+964', '+353', '+972',
            '+39', '+1876', '+81', '+962', '+7', '+254', '+686', '+383', '+965', '+996', '+856', '+371',
            '+961', '+266', '+231', '+218', '+423', '+370', '+352', '+853', '+261', '+265', '+60', '+960',
            '+223', '+356', '+692', '+596', '+222', '+230', '+52', '+691', '+373', '+377', '+976', '+382',
            '+1664', '+212', '+258', '+95', '+264', '+674', '+977', '+31', '+687', '+64', '+505', '+227',
            '+234', '+683', '+672', '+850', '+389', '+1670', '+47', '+968', '+92', '+680', '+970', '+507',
            '+675', '+595', '+51', '+63', '+48', '+351', '+1787', '+1939', '+974', '+262', '+40', '+7',
            '+250', '+247', '+290', '+1869', '+1758', '+508', '+1784', '+685', '+378', '+239', '+966',
            '+221', '+381', '+248', '+232', '+65', '+1721', '+421', '+386', '+677', '+252', '+27', '+82',
            '+211', '+34', '+94', '+249', '+597', '+46', '+41', '+963', '+886', '+992', '+255', '+66',
            '+670', '+228', '+690', '+676', '+1868', '+216', '+90', '+993', '+1649', '+688', '+256',
            '+380', '+971', '+44', '+598', '+1340', '+1', '+998', '+678', '+58', '+84', '+681', '+967',
            '+260', '+263'
        ]
        prev = cellphone[:-10]
        rest = cellphone[:-11:-1][::-1]
        if not rest.isnumeric():
            raise ValueError('شماره تلفن نباید شامل حروف باشد')
        if prev not in prev_numbers:
            raise ValueError('کد کشور صحیح نیست')
        if rest.__len__() != 10:
            raise ValueError('شماره تلفن باید ۱۰ رقم داشته باشد')
        return cellphone
