from rest_framework.serializers import ModelSerializer,SerializerMethodField

from server.target.models.user import Employer
from server.target.models.jobs import Job




class EmployersRegistrationSerializer(ModelSerializer):
    """
    employers registration serializer class
    """

    class Meta:
        model = Employer
        fields = [
            'email', 'first_name', 'last_name', 'password', "company_name",
            "company_size", "phone","description", "user_type"
        ]
        read_only_fields = ("user_type",)

class EmployersCompanyInfoSerializer(ModelSerializer):
    """
    Serializer class to return company info
    """

    class Meta:
        model = Employer
        fields = [
            "id","company_name", "company_size","description"
        ]
        
class TopCompaniesSerializer(ModelSerializer):
    """
    Serializer class to return top companies based on number of jobs
    """
    jobs = SerializerMethodField()

    class Meta:
        model = Employer
        fields = [
            "id", "company_name", "company_size", "description", "jobs"
        ]
    
    def get_jobs(self, obj:Employer):
        return len(Job.objects.filter(company__id = obj.id).select_related('company'))

class EmployersDetailsSerializer(ModelSerializer):
    """
    employers details serializer class
    """
    jobs = SerializerMethodField()
    most_recent = SerializerMethodField()

    class Meta:
        model = Employer
        fields = [
            "id",'email', 'first_name', 'last_name', "company_name",
            "company_size", "phone","description", "user_type",
            "jobs","most_recent"
        ]
        read_only_fields = ("user_type",)
    
    def get_jobs(self, obj: Employer) -> Job:
        """
        This method will return all of jobs that was posted by employer
        """
        from server.target.serializers.jobs import JobSearchSerializers
        jobs = Job.objects.filter(
            company__id = obj.id
        )
        return JobSearchSerializers(jobs, many=True).data
    
    def get_most_recent(self, obj):
        """Return True if most recent else False"""
        from datetime import datetime, date
        if date.today() == obj.created.date():
            return True if int(datetime.now().hour) - (int(obj.created.hour) + 2) <= 1 else False