from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/", json={"service_ip": "http://127.0.0.1:5000/rni/v2/queries/rab_info/1",
                                    "cell_user_info": {
                                            "ecgi": {
                                                "cell_id":  "cell_02154",
                                                "plmn" :{
                                                    "mcc" : "mcc",
                                                    "mnc" : "mnc"
                                                }
                                            },
                                            "ue_info": {
                                                "associate_id": {
                                                    "type": "1",
                                                    "value": "constante"
                                                },
                                                "erab_info": {
                                                    "erab_id": 1,
                                                    "erab_qos_parameters": {
                                                        "qci": 1,
                                                        "qos_information": {
                                                            "erab_gbr_dl": 1,
                                                            "erab_gbr_ul": 1,
                                                            "erab_mbr_dl": 1,
                                                            "erab_mbr_ul": 1
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "request_id": "1",
                                        "time_stamp": {
                                            "nano_seconds": 12,
                                            "seconds": 13
                                        }
                                    })