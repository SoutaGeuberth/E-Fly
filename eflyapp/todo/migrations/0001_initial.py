# Generated by Django 4.2 on 2023-05-02 17:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('DNI', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('saldo', models.IntegerField(default=0)),
                ('fechaNaci', models.DateField(null=True)),
                ('lugarNaci', models.CharField(max_length=50, null=True)),
                ('dirFact', models.CharField(max_length=100, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra'), ('N', 'No Responde')], default='N', max_length=20)),
                ('tipoUsuario', models.CharField(max_length=20, null=True)),
                ('picture', models.ImageField(default='profile_default.png', upload_to='users/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(default=10)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('texto', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaSalida', models.TimeField()),
                ('horaLlegada', models.TimeField()),
                ('precioPrimera', models.IntegerField()),
                ('precioEconomica', models.IntegerField()),
                ('precioPrimeraDesc', models.IntegerField()),
                ('precioEconomicaDesc', models.IntegerField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinos', to='todo.ciudad')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origenes', to='todo.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePasajero', models.CharField(max_length=50)),
                ('emailPasajero', models.EmailField(max_length=254)),
                ('edadPasajero', models.IntegerField()),
                ('asiento', models.CharField(max_length=4)),
                ('clase', models.CharField(choices=[('p', 'Primera Clase'), ('e', 'Clase Economica')], max_length=20)),
                ('EstadoCheckIn', models.CharField(default='No Realizado', max_length=15)),
                ('Compraid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compraid', to='todo.compra')),
                ('Vueloid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vueloid', to='todo.vuelo')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('d', 'debito'), ('c', 'credito')], max_length=20)),
                ('disponible', models.IntegerField(default=200000)),
                ('numero', models.CharField(max_length=16)),
                ('nombre', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('vencimiento', models.DateField()),
                ('clienteid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
