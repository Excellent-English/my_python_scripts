import pandas as pd

# Dane o zawodniku
data = {
      "player": {
        "id": 35323828,
        "info": {
          "name": {
            "name": "Jimmy",
            "surname": "Patricsson",
            "full": "Jimmy Patricsson"
          },
          "formation": null,
          "number": null,
          "team": {
            "id": 70787,
            "name": "FC Lacusteni",
            "rank": 4030.33,
            "rankPosition": 330,
            "emblem": "/team-emblem-70787.png",
            "country": {
              "code": 9,
              "name": "România"
            },
            "colors": {
              "first": {
                "shirt": {
                  "hex": "#e0c657"
                },
                "trousers": {
                  "hex": "#1103d2"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              },
              "second": {
                "shirt": {
                  "hex": "#6f55a6"
                },
                "trousers": {
                  "hex": "#1103d2"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              },
              "keeper": {
                "shirt": {
                  "hex": "#000000"
                },
                "trousers": {
                  "hex": "#000000"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              }
            },
            "nationalType": 0,
            "bankrupt": false
          },
          "country": {
            "code": 31,
            "name": "Sverige"
          },
          "value": {
            "value": 512000,
            "currency": "zł"
          },
          "previousValue": null,
          "wage": {
            "value": 7300,
            "currency": "zł"
          },
          "characteristics": {
            "age": 47,
            "height": 179,
            "weight": 85.1935,
            "bmi": 26.58890171967167
          },
          "skills": {
            "form": 0,
            "tacticalDiscipline": 10,
            "teamwork": 4,
            "experience": 17,
            "stamina": 6,
            "keeper": 9,
            "playmaking": 0,
            "passing": 0,
            "technique": 0,
            "defending": 0,
            "striker": 0,
            "pace": 1
          },
          "stats": {
            "cards": {
              "cards": 0,
              "yellow": 0,
              "red": 0
            },
            "goals": 1,
            "assists": 0,
            "matches": 366
          },
          "nationalStats": {
            "cards": {
              "cards": 0,
              "yellow": 0,
              "red": 0
            },
            "goals": 0,
            "assists": 0,
            "matches": 1
          },
          "face": {
            "face": 1,
            "skinColor": 1,
            "hairColor": 5,
            "hair": 2,
            "eyes": 9,
            "nose": 6,
            "beard": 9,
            "beardColor": 8,
            "shirt": 1,
            "mouth": 3
          },
          "youthTeamId": 84828,
          "injury": {
            "daysRemaining": 0,
            "severe": false
          },
          "nationalSharing": true
        }
      },
      "deadline": {
        "date": {
          "date": "2025-01-11 13:46:05.000000",
          "timezone_type": 3,
          "timezone": "Europe/Warsaw"
        },
        "secondsLeft": 102417,
        "daysLeft": 1
      },
      "ended": false,
      "price": {
        "listed": {
          "value": 1,
          "currency": "zł"
        },
        "bid": {
          "value": 0,
          "currency": "zł"
        },
        "minBid": {
          "value": 1,
          "currency": "zł"
        },
        "suggestedBid": {
          "value": 1000,
          "currency": "zł"
        }
      },
      "buyer": null,
      "observers": 0
    },
    {
      "player": {
        "id": 35894249,
        "info": {
          "name": {
            "name": "Moreno",
            "surname": "Gaudin",
            "full": "Moreno Gaudin"
          },
          "formation": null,
          "number": null,
          "team": {
            "id": 71648,
            "name": "odette fc",
            "rank": 4023.05,
            "rankPosition": 332,
            "emblem": "/team-emblem-71648.png",
            "country": {
              "code": 9,
              "name": "România"
            },
            "colors": {
              "first": {
                "shirt": {
                  "hex": "#e0c657"
                },
                "trousers": {
                  "hex": "#1103d2"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              },
              "second": {
                "shirt": {
                  "hex": "#6f55a6"
                },
                "trousers": {
                  "hex": "#1103d2"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              },
              "keeper": {
                "shirt": {
                  "hex": "#000000"
                },
                "trousers": {
                  "hex": "#000000"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              }
            },
            "nationalType": 0,
            "bankrupt": false
          },
          "country": {
            "code": 24,
            "name": "Schweiz"
          },
          "value": {
            "value": 592000,
            "currency": "zł"
          },
          "previousValue": null,
          "wage": {
            "value": 13100,
            "currency": "zł"
          },
          "characteristics": {
            "age": 43,
            "height": 169,
            "weight": 65.5894,
            "bmi": 22.964672105318442
          },
          "skills": {
            "form": 9,
            "tacticalDiscipline": 12,
            "teamwork": 7,
            "experience": 17,
            "stamina": 11,
            "keeper": 0,
            "playmaking": 6,
            "passing": 5,
            "technique": 9,
            "defending": 0,
            "striker": 3,
            "pace": 9
          },
          "stats": {
            "cards": {
              "cards": 1,
              "yellow": 1,
              "red": 0
            },
            "goals": 19,
            "assists": 105,
            "matches": 329
          },
          "nationalStats": {
            "cards": {
              "cards": 1,
              "yellow": 1,
              "red": 0
            },
            "goals": 0,
            "assists": 0,
            "matches": 9
          },
          "face": {
            "face": 1,
            "skinColor": 2,
            "hairColor": 3,
            "hair": 3,
            "eyes": 5,
            "nose": 4,
            "beard": 0,
            "beardColor": 4,
            "shirt": 1,
            "mouth": 4
          },
          "youthTeamId": 6731,
          "injury": {
            "daysRemaining": 0,
            "severe": false
          },
          "nationalSharing": true
        }
      },
      "deadline": {
        "date": {
          "date": "2025-01-11 15:35:57.000000",
          "timezone_type": 3,
          "timezone": "Europe/Warsaw"
        },
        "secondsLeft": 109009,
        "daysLeft": 1
      },
      "ended": false,
      "price": {
        "listed": {
          "value": 11499,
          "currency": "zł"
        },
        "bid": {
          "value": 0,
          "currency": "zł"
        },
        "minBid": {
          "value": 11499,
          "currency": "zł"
        },
        "suggestedBid": {
          "value": 12000,
          "currency": "zł"
        }
      },
      "buyer": null,
      "observers": 0
    },
    {
      "player": {
        "id": 36374276,
        "info": {
          "name": {
            "name": "Zmitrok",
            "surname": "Sumich",
            "full": "Zmitrok Sumich"
          },
          "formation": null,
          "number": null,
          "team": {
            "id": 31049,
            "name": "__BEŞİKTAŞK__",
            "rank": 6067.7,
            "rankPosition": 3,
            "emblem": "/team-emblem-31049.png",
            "country": {
              "code": 41,
              "name": "Türkiye"
            },
            "colors": {
              "first": {
                "shirt": {
                  "hex": "#000000"
                },
                "trousers": {
                  "hex": "#000000"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              },
              "second": {
                "shirt": {
                  "hex": "#ffffff"
                },
                "trousers": {
                  "hex": "#ffffff"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              },
              "keeper": {
                "shirt": {
                  "hex": "#000000"
                },
                "trousers": {
                  "hex": "#000000"
                },
                "type": {
                  "code": 0,
                  "name": "blank"
                }
              }
            },
            "nationalType": 0,
            "bankrupt": false
          },
          "country": {
            "code": 46,
            "name": "Belarus"
          },
          "value": {
            "value": 1927000,
            "currency": "zł"
          },
          "previousValue": null,
          "wage": {
            "value": 30600,
            "currency": "zł"
          },
          "characteristics": {
            "age": 40,
            "height": 184,
            "weight": 78.9746,
            "bmi": 23.326618620037806
          },
          "skills": {
            "form": 10,
            "tacticalDiscipline": 10,
            "teamwork": 3,
            "experience": 18,
            "stamina": 11,
            "keeper": 0,
            "playmaking": 4,
            "passing": 4,
            "technique": 13,
            "defending": 4,
            "striker": 11,
            "pace": 13
          },
          "stats": {
            "cards": {
              "cards": 0,
              "yellow": 0,
              "red": 0
            },
            "goals": 833,
            "assists": 122,
            "matches": 408
          },
          "nationalStats": {
            "cards": {
              "cards": 2,
              "yellow": 2,
              "red": 0
            },
            "goals": 122,
            "assists": 12,
            "matches": 258
          },
          "face": {
            "face": 3,
            "skinColor": 1,
            "hairColor": 1,
            "hair": 0,
            "eyes": 5,
            "nose": 8,
            "beard": 5,
            "beardColor": 1,
            "shirt": 1,
            "mouth": 5
          },
          "youthTeamId": 0,
          "injury": {
            "daysRemaining": 0,
            "severe": false
          },
          "nationalSharing": true
        }
      },
      "deadline": {
        "date": {
          "date": "2025-01-10 23:09:11.000000",
          "timezone_type": 3,
          "timezone": "Europe/Warsaw"
        },
        "secondsLeft": 49803,
        "daysLeft": 0
      },
      "ended": false,
      "price": {
        "listed": {
          "value": 5,
          "currency": "zł"
        },
        "bid": {
          "value": 1000,
          "currency": "zł"
        },
        "minBid": {
          "value": 6000,
          "currency": "zł"
        },
        "suggestedBid": {
          "value": 6000,
          "currency": "zł"
        }
      },
      "buyer": {
        "id": 3497,
        "name": "LKS tęcza Zendek 1973!!",
        "rank": 2666.7,
        "rankPosition": 2129,
        "emblem": "/team-emblem-3497.png",
        "country": {
          "code": 1,
          "name": "Polska"
        },
        "colors": {
          "first": {
            "shirt": {
              "hex": "#e0c657"
            },
            "trousers": {
              "hex": "#1103d2"
            },
            "type": {
              "code": 0,
              "name": "blank"
            }
          },
          "second": {
            "shirt": {
              "hex": "#070c08"
            },
            "trousers": {
              "hex": "#11030c"
            },
            "type": {
              "code": 1,
              "name": "stripped"
            }
          },
          "keeper": {
            "shirt": {
              "hex": "#de2026"
            },
            "trousers": {
              "hex": "#000001"
            },
            "type": {
              "code": 0,
              "name": "blank"
            }
          }
        },
        "nationalType": 0,
        "bankrupt": false
      },
      "observers": 1
    }
        }
    }
}

# Przekształcenie danych do formatu DataFrame
player_info = data['player']['info']

# Konwersja zagnieżdżonych słowników na płaską strukturę
flat_data = {}
for key, value in player_info.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            flat_data[f"{key}_{sub_key}"] = sub_value
    else:
        flat_data[key] = value

df = pd.DataFrame([flat_data])

# Zapisanie danych do pliku Excel
df.to_excel('player_info.xlsx', index=False)

print("Dane zawodnika zostały zapisane w pliku player_info.xlsx.")