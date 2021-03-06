# Generated by Django 3.1.4 on 2020-12-25 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignsTextbook',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('semester', models.IntegerField(db_column='Semester')),
            ],
            options={
                'db_table': 'ASSIGNS_TEXTBOOK',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendsClass',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('result', models.JSONField(blank=True, db_column='Result', null=True)),
            ],
            options={
                'db_table': 'ATTENDS_CLASS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('authorid', models.AutoField(db_column='AuthorId', primary_key=True, serialize=False)),
                ('authorname', models.CharField(db_column='AuthorName', max_length=255)),
            ],
            options={
                'db_table': 'AUTHOR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('semester', models.IntegerField(db_column='Semester')),
                ('classid', models.CharField(db_column='ClassId', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'CLASS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.CharField(db_column='CourseId', max_length=6, primary_key=True, serialize=False)),
                ('coursename', models.CharField(db_column='CourseName', max_length=255)),
                ('credits', models.JSONField(db_column='Credits')),
            ],
            options={
                'db_table': 'COURSE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('departmentno', models.AutoField(db_column='DepartmentNo', primary_key=True, serialize=False)),
                ('departmentname', models.CharField(db_column='DepartmentName', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'DEPARTMENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enrolls',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('semester', models.IntegerField(db_column='Semester')),
            ],
            options={
                'db_table': 'ENROLLS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagesClass',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'MANAGES_CLASS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagesCourse',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('semester', models.IntegerField(db_column='Semester')),
            ],
            options={
                'db_table': 'MANAGES_COURSE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisherid', models.AutoField(db_column='PublisherId', primary_key=True, serialize=False)),
                ('publishername', models.CharField(db_column='PublisherName', max_length=255)),
            ],
            options={
                'db_table': 'PUBLISHER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publishes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('publisheddate', models.DateTimeField(blank=True, db_column='PublishedDate', null=True)),
            ],
            options={
                'db_table': 'PUBLISHES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('week', models.IntegerField(db_column='Week')),
            ],
            options={
                'db_table': 'TEACHES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('isbn', models.DecimalField(db_column='Isbn', decimal_places=0, max_digits=13, primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=255)),
                ('field', models.CharField(blank=True, db_column='Field', max_length=255, null=True)),
            ],
            options={
                'db_table': 'TEXTBOOK',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uses',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'USES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Writes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'WRITES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.DecimalField(db_column='StudentId', decimal_places=0, max_digits=7, primary_key=True, serialize=False)),
                ('studentname', models.CharField(db_column='StudentName', max_length=255)),
                ('currentstatus', models.CharField(db_column='CurrentStatus', max_length=9)),
                ('departmentno', models.ForeignKey(blank=True, db_column='DepartmentNo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='administrator.department')),
            ],
            options={
                'db_table': 'STUDENT',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lecturerid', models.DecimalField(db_column='LecturerId', decimal_places=0, max_digits=7, primary_key=True, serialize=False)),
                ('lecturername', models.CharField(db_column='LecturerName', max_length=255)),
                ('departmentno', models.ForeignKey(blank=True, db_column='DepartmentNo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='administrator.department')),
            ],
            options={
                'db_table': 'LECTURER',
                'managed': True,
            },
        ),
    ]
