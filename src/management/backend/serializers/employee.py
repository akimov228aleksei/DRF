from ..models.employee import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """Data serialization class for the whole list of records"""
    position = serializers.CharField()
    department = serializers.CharField()

    class Meta:
        model = Employee
        fields = ('url', 'first_name', 'second_name', 'department', 'position')


class EmployeeDetailSerializer(serializers.ModelSerializer):
    """Single entry data serialization class"""
    position_title = serializers.CharField(source='position.title', read_only=True)
    department_title = serializers.CharField(source='department.title', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
