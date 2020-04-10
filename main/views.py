from rest_framework.views import APIView
from rest_framework.response import Response
from .system_info import (
    system_information,
    boot_time,
    cpu_info,
    virtual_memory,
    swap_memory,
    disk_info,
    network_info,
    battery_info,
    temperature_info
)

class HealthCheckView(APIView):
    def get(self, request):
        Response.status_code = 200
        return Response({
            "status": "success",
            "message": "Server is working fine"
        })


choices = {
    1: "System Information",
    2: "Boot Info",
    3: "Cpu Info",
    4: "Virtual Memory Info",
    5: "Swap Memory",
    6: "Disk Info",
    7: "Network Info",
    8: "Battery Info"
}


class AvailableSystemMonitoringChoices(APIView):
    def get(self, request):
        return Response({
            "choice": choices.values()
        })


class ReturningSystemDataView(APIView):
    def get(self, request):
        choice = request.query_params.get('metric')
        if choice == choices[1]:
            return Response(system_information())
        elif choice == choices[2]:
            return Response(boot_time())
        elif choice == choices[3]:
            return Response(cpu_info())
        elif choice == choices[4]:
            return Response(virtual_memory())
        elif choice == choices[5]:
            return Response(swap_memory())
        elif choice == choices[6]:
            return Response(disk_info())
        elif choice == choices[7]:
            return Response(network_info())
        elif choice == choices[8]:
            return Response(battery_info)
        elif choice == 'All':
            return Response({
                choices[1]: system_information(),
                choices[2]: boot_time(),
                choices[3]: cpu_info(),
                choices[4]: virtual_memory(),
                choices[5]: swap_memory(),
                choices[6]: disk_info(),
                choices[7]: network_info(),
                choices[8]: battery_info()
            })
        else:
            return Response({
              "status": "error, query parameter incorrect, missing or invalid"  
            })
