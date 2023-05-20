from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    
    @task
    def recommender1(self):
        self.client.post("recommender1", json={"results": [
        {
            "slug": "god-of-war-ragnarok",
            "name": "God of War: Ragnarök",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2022-11-09",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/1c3/1c305096502c475c00276c827f0fd697.jpg",
            "rating": 4.6,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 203,
                    "percent": 73.82
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 53,
                    "percent": 19.27
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 10,
                    "percent": 3.64
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 9,
                    "percent": 3.27
                }
            ],
            "ratings_count": 260,
            "reviews_text_count": 11,
            "added": 1237,
            "added_by_status": {
                "yet": 168,
                "owned": 153,
                "beaten": 256,
                "toplay": 588,
                "dropped": 9,
                "playing": 63
            },
            "metacritic": 94,
            "suggestions_count": 494,
            "updated": "2023-04-16T07:19:47",
            "id": 494384,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 37797,
                    "name": "true exclusive",
                    "slug": "true-exclusive",
                    "language": "eng",
                    "games_count": 3995,
                    "image_background": "https://media.rawg.io/media/games/214/214b29aeff13a0ae6a70fc4426e85991.jpg"
                },
                {
                    "id": 425,
                    "name": "Single player only",
                    "slug": "single-player-only",
                    "language": "eng",
                    "games_count": 31,
                    "image_background": "https://media.rawg.io/media/games/862/86283a28784f6a24d35b5bbb3ab3b4a8.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 275,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/1c3/1c305096502c475c00276c827f0fd697.jpg"
                },
                {
                    "id": 3024359,
                    "image": "https://media.rawg.io/media/screenshots/55f/55fe715e129d5365b48b35b5fc8052be.jpg"
                },
                {
                    "id": 3024360,
                    "image": "https://media.rawg.io/media/screenshots/c3e/c3e2f128960ffdac8d91f097ebf213e4.jpg"
                },
                {
                    "id": 3024361,
                    "image": "https://media.rawg.io/media/screenshots/ab5/ab5dce69619658d010c7342523c63d69_fmTr8dx.jpg"
                },
                {
                    "id": 3024362,
                    "image": "https://media.rawg.io/media/screenshots/d19/d193a94e600261aa6a35883ae7258687.jpg"
                },
                {
                    "id": 3024363,
                    "image": "https://media.rawg.io/media/screenshots/87d/87d0502ad973a922615bb585ead18661.jpg"
                },
                {
                    "id": 3024364,
                    "image": "https://media.rawg.io/media/screenshots/001/00156acba9a5a3316893c22f4bd15edf.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "red-dead-redemption-2",
            "name": "Red Dead Redemption 2",
            "playtime": 18,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 11,
                        "name": "Epic Games",
                        "slug": "epic-games"
                    }
                }
            ],
            "released": "2018-10-26",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg",
            "rating": 4.59,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 3345,
                    "percent": 73.29
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 831,
                    "percent": 18.21
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 255,
                    "percent": 5.59
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 133,
                    "percent": 2.91
                }
            ],
            "ratings_count": 4474,
            "reviews_text_count": 65,
            "added": 13912,
            "added_by_status": {
                "yet": 842,
                "owned": 7311,
                "beaten": 2767,
                "toplay": 1531,
                "dropped": 590,
                "playing": 871
            },
            "metacritic": 96,
            "suggestions_count": 577,
            "updated": "2023-04-16T07:19:57",
            "id": 28,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 18,
                    "name": "Co-op",
                    "slug": "co-op",
                    "language": "eng",
                    "games_count": 9806,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42442,
                    "name": "Открытый мир",
                    "slug": "otkrytyi-mir",
                    "language": "rus",
                    "games_count": 4297,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42428,
                    "name": "Шутер",
                    "slug": "shuter",
                    "language": "rus",
                    "games_count": 6479,
                    "image_background": "https://media.rawg.io/media/games/c24/c24ec439abf4a2e92f3429dfa83f7f94.jpg"
                },
                {
                    "id": 8,
                    "name": "First-Person",
                    "slug": "first-person",
                    "language": "eng",
                    "games_count": 29966,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 42435,
                    "name": "Шедевр",
                    "slug": "shedevr",
                    "language": "rus",
                    "games_count": 1059,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 40845,
                    "name": "Partial Controller Support",
                    "slug": "partial-controller-support",
                    "language": "eng",
                    "games_count": 9594,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 30,
                    "name": "FPS",
                    "slug": "fps",
                    "language": "eng",
                    "games_count": 12754,
                    "image_background": "https://media.rawg.io/media/games/f87/f87457e8347484033cb34cde6101d08d.jpg"
                },
                {
                    "id": 42427,
                    "name": "Шутер от первого лица",
                    "slug": "shuter-ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 3952,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 9,
                    "name": "Online Co-Op",
                    "slug": "online-co-op",
                    "language": "eng",
                    "games_count": 4246,
                    "image_background": "https://media.rawg.io/media/games/d69/d69810315bd7e226ea2d21f9156af629.jpg"
                },
                {
                    "id": 42491,
                    "name": "Мясо",
                    "slug": "miaso",
                    "language": "rus",
                    "games_count": 3850,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 26,
                    "name": "Gore",
                    "slug": "gore",
                    "language": "eng",
                    "games_count": 5083,
                    "image_background": "https://media.rawg.io/media/games/998/9980c4296f311d8bcc5b451ca51e4fe1.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 37,
                    "name": "Sandbox",
                    "slug": "sandbox",
                    "language": "eng",
                    "games_count": 6073,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42444,
                    "name": "Песочница",
                    "slug": "pesochnitsa",
                    "language": "rus",
                    "games_count": 3023,
                    "image_background": "https://media.rawg.io/media/games/4a0/4a0a1316102366260e6f38fd2a9cfdce.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 42446,
                    "name": "Шутер от третьего лица",
                    "slug": "shuter-ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 1437,
                    "image_background": "https://media.rawg.io/media/games/ebd/ebdbb7eb52bd58b0e7fa4538d9757b60.jpg"
                },
                {
                    "id": 150,
                    "name": "Third-Person Shooter",
                    "slug": "third-person-shooter",
                    "language": "eng",
                    "games_count": 2936,
                    "image_background": "https://media.rawg.io/media/games/a6c/a6ccd34125c594abf1a9c9821b9a715d.jpg"
                },
                {
                    "id": 157,
                    "name": "PvP",
                    "slug": "pvp",
                    "language": "eng",
                    "games_count": 7102,
                    "image_background": "https://media.rawg.io/media/games/9c4/9c47f320eb73c9a02d462e12f6206b26.jpg"
                },
                {
                    "id": 40837,
                    "name": "In-App Purchases",
                    "slug": "in-app-purchases",
                    "language": "eng",
                    "games_count": 2022,
                    "image_background": "https://media.rawg.io/media/games/d0f/d0f91fe1d92332147e5db74e207cfc7a.jpg"
                },
                {
                    "id": 42529,
                    "name": "Для взрослых",
                    "slug": "dlia-vzroslykh",
                    "language": "rus",
                    "games_count": 1877,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 192,
                    "name": "Mature",
                    "slug": "mature",
                    "language": "eng",
                    "games_count": 2065,
                    "image_background": "https://media.rawg.io/media/games/c81/c812e158129e00c9b0f096ae8a0bb7d6.jpg"
                },
                {
                    "id": 42460,
                    "name": "Реализм",
                    "slug": "realizm",
                    "language": "rus",
                    "games_count": 3621,
                    "image_background": "https://media.rawg.io/media/games/bff/bff7d82316cddea9541261a045ba008a.jpg"
                },
                {
                    "id": 89,
                    "name": "Historical",
                    "slug": "historical",
                    "language": "eng",
                    "games_count": 2635,
                    "image_background": "https://media.rawg.io/media/games/d8f/d8f3b28fc747ed6f92943cdd33fb91b5.jpeg"
                },
                {
                    "id": 110,
                    "name": "Cinematic",
                    "slug": "cinematic",
                    "language": "eng",
                    "games_count": 1313,
                    "image_background": "https://media.rawg.io/media/games/7ac/7aca7ccf0e70cd0974cb899ab9e5158e.jpg"
                },
                {
                    "id": 77,
                    "name": "Realistic",
                    "slug": "realistic",
                    "language": "eng",
                    "games_count": 3658,
                    "image_background": "https://media.rawg.io/media/games/106/1069e754e7e6012b0cf42b4b04704792.jpg"
                },
                {
                    "id": 144,
                    "name": "Crime",
                    "slug": "crime",
                    "language": "eng",
                    "games_count": 2580,
                    "image_background": "https://media.rawg.io/media/games/9e5/9e5b274c7e3aa5e30beba31b834b0e7e.jpg"
                },
                {
                    "id": 42690,
                    "name": "Красивая",
                    "slug": "krasivaia",
                    "language": "rus",
                    "games_count": 537,
                    "image_background": "https://media.rawg.io/media/games/90c/90caf1fcb836cad70013452f6f239008.jpg"
                },
                {
                    "id": 45878,
                    "name": "Online PvP",
                    "slug": "online-pvp",
                    "language": "eng",
                    "games_count": 3021,
                    "image_background": "https://media.rawg.io/media/games/c3b/c3be1d5f55cb9324c97ccb7aaaf42ad4.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 86,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 270,
                    "name": "Blood",
                    "slug": "blood",
                    "language": "eng",
                    "games_count": 1984,
                    "image_background": "https://media.rawg.io/media/games/63f/63f0e68688cad279ed38cde931dbfcdb.jpg"
                },
                {
                    "id": 78,
                    "name": "America",
                    "slug": "america",
                    "language": "eng",
                    "games_count": 440,
                    "image_background": "https://media.rawg.io/media/games/4c2/4c23c4a88f53e7e482d72ddfcf5b9b41.jpg"
                },
                {
                    "id": 578,
                    "name": "Masterpiece",
                    "slug": "masterpiece",
                    "language": "eng",
                    "games_count": 276,
                    "image_background": "https://media.rawg.io/media/games/0fa/0fa9e2b8397b332902d3b56c73888d52.jpg"
                },
                {
                    "id": 577,
                    "name": "Beautiful",
                    "slug": "beautiful",
                    "language": "eng",
                    "games_count": 1820,
                    "image_background": "https://media.rawg.io/media/games/d3e/d3ee2d7653cf9d4640335ff7a471ab07.jpg"
                },
                {
                    "id": 181,
                    "name": "Hunting",
                    "slug": "hunting",
                    "language": "eng",
                    "games_count": 839,
                    "image_background": "https://media.rawg.io/media/games/bf7/bf73b105ccbba42107986bbcd96fcada.jpg"
                },
                {
                    "id": 152,
                    "name": "Western",
                    "slug": "western",
                    "language": "eng",
                    "games_count": 1275,
                    "image_background": "https://media.rawg.io/media/screenshots/d2d/d2da7735c7f8a2a765c4649a650e2c30.jpg"
                },
                {
                    "id": 42475,
                    "name": "Вестерн",
                    "slug": "vestern",
                    "language": "rus",
                    "games_count": 253,
                    "image_background": "https://media.rawg.io/media/games/e07/e07737df8469bf32d132ba9eaffc3461.jpg"
                },
                {
                    "id": 5452,
                    "name": "3rd-person",
                    "slug": "3rd-person",
                    "language": "eng",
                    "games_count": 97,
                    "image_background": "https://media.rawg.io/media/screenshots/e30/e30b6a334c20ae534c15d3f0d71cad36.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 4564,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 778173,
                    "image": "https://media.rawg.io/media/screenshots/7b8/7b8895a23e8ca0dbd9e1ba24696579d9.jpg"
                },
                {
                    "id": 778174,
                    "image": "https://media.rawg.io/media/screenshots/b8c/b8cee381079d58b981594ede46a3d6ca.jpg"
                },
                {
                    "id": 778175,
                    "image": "https://media.rawg.io/media/screenshots/fd6/fd6e41d4c30c098158568aef32dfed35.jpg"
                },
                {
                    "id": 778176,
                    "image": "https://media.rawg.io/media/screenshots/2ed/2ed3b2791b3bbed6b98bf362694aeb73.jpg"
                },
                {
                    "id": 778177,
                    "image": "https://media.rawg.io/media/screenshots/857/8573b9f4f06a0c112d6e39cdf3544881.jpg"
                },
                {
                    "id": 778178,
                    "image": "https://media.rawg.io/media/screenshots/985/985e3e1f1d1af1ab0797d43a95d472cc.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "god-of-war-2",
            "name": "God of War (2018)",
            "playtime": 10,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 11,
                        "name": "Epic Games",
                        "slug": "epic-games"
                    }
                }
            ],
            "released": "2018-04-20",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg",
            "rating": 4.59,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 3183,
                    "percent": 72.39
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 881,
                    "percent": 20.04
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 197,
                    "percent": 4.48
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 136,
                    "percent": 3.09
                }
            ],
            "ratings_count": 4312,
            "reviews_text_count": 62,
            "added": 12229,
            "added_by_status": {
                "yet": 624,
                "owned": 6269,
                "beaten": 3560,
                "toplay": 1086,
                "dropped": 279,
                "playing": 411
            },
            "metacritic": 94,
            "suggestions_count": 577,
            "updated": "2023-04-16T19:09:16",
            "id": 58175,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 24,
                    "name": "RPG",
                    "slug": "rpg",
                    "language": "eng",
                    "games_count": 17009,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 42412,
                    "name": "Ролевая игра",
                    "slug": "rolevaia-igra",
                    "language": "rus",
                    "games_count": 13302,
                    "image_background": "https://media.rawg.io/media/games/ee3/ee3e10193aafc3230ba1cae426967d10.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 42480,
                    "name": "Фэнтези",
                    "slug": "fentezi",
                    "language": "rus",
                    "games_count": 7813,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 64,
                    "name": "Fantasy",
                    "slug": "fantasy",
                    "language": "eng",
                    "games_count": 25175,
                    "image_background": "https://media.rawg.io/media/games/33d/33df5a032898b8ab7e3773c7a5f1d336.jpg"
                },
                {
                    "id": 42491,
                    "name": "Мясо",
                    "slug": "miaso",
                    "language": "rus",
                    "games_count": 3850,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 26,
                    "name": "Gore",
                    "slug": "gore",
                    "language": "eng",
                    "games_count": 5083,
                    "image_background": "https://media.rawg.io/media/games/998/9980c4296f311d8bcc5b451ca51e4fe1.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 97,
                    "name": "Action RPG",
                    "slug": "action-rpg",
                    "language": "eng",
                    "games_count": 5874,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 42489,
                    "name": "Ролевой экшен",
                    "slug": "rolevoi-ekshen",
                    "language": "rus",
                    "games_count": 2557,
                    "image_background": "https://media.rawg.io/media/games/5be/5bec14622f6faf804a592176577c1347.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42487,
                    "name": "Слэшер",
                    "slug": "slesher",
                    "language": "rus",
                    "games_count": 1862,
                    "image_background": "https://media.rawg.io/media/games/21a/21ad672cedee9b4378abb6c2d2e626ee.jpg"
                },
                {
                    "id": 68,
                    "name": "Hack and Slash",
                    "slug": "hack-and-slash",
                    "language": "eng",
                    "games_count": 3414,
                    "image_background": "https://media.rawg.io/media/games/af7/af7a831001c5c32c46e950cc883b8cb7.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 125,
                    "name": "Crafting",
                    "slug": "crafting",
                    "language": "eng",
                    "games_count": 3399,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 42497,
                    "name": "Крафтинг",
                    "slug": "krafting",
                    "language": "rus",
                    "games_count": 1982,
                    "image_background": "https://media.rawg.io/media/games/8a7/8a75028028592f9323d1e6e86668bb91.jpg"
                },
                {
                    "id": 37797,
                    "name": "true exclusive",
                    "slug": "true-exclusive",
                    "language": "eng",
                    "games_count": 3995,
                    "image_background": "https://media.rawg.io/media/games/214/214b29aeff13a0ae6a70fc4426e85991.jpg"
                },
                {
                    "id": 1465,
                    "name": "combat",
                    "slug": "combat",
                    "language": "eng",
                    "games_count": 9132,
                    "image_background": "https://media.rawg.io/media/games/0a5/0a56e2bb9ce95359e69ff9689c553a45.jpg"
                },
                {
                    "id": 571,
                    "name": "3D",
                    "slug": "3d",
                    "language": "eng",
                    "games_count": 81983,
                    "image_background": "https://media.rawg.io/media/screenshots/066/066eb1b7a3f332b8089645fbf8c3ebdc.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 86,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 270,
                    "name": "Blood",
                    "slug": "blood",
                    "language": "eng",
                    "games_count": 1984,
                    "image_background": "https://media.rawg.io/media/games/63f/63f0e68688cad279ed38cde931dbfcdb.jpg"
                },
                {
                    "id": 42567,
                    "name": "Игра против ИИ",
                    "slug": "igra-protiv-ii",
                    "language": "rus",
                    "games_count": 2346,
                    "image_background": "https://media.rawg.io/media/screenshots/6d3/6d367773c06886535620f2d7fb1cb866.jpg"
                },
                {
                    "id": 42592,
                    "name": "Похожа на Dark Souls",
                    "slug": "pokhozha-na-dark-souls",
                    "language": "rus",
                    "games_count": 605,
                    "image_background": "https://media.rawg.io/media/games/718/71891d2484a592d871e91dc826707e1c.jpg"
                },
                {
                    "id": 171,
                    "name": "PvE",
                    "slug": "pve",
                    "language": "eng",
                    "games_count": 2925,
                    "image_background": "https://media.rawg.io/media/games/bde/bdef96f7782fba0ff62dabc37ff4b1f0.jpg"
                },
                {
                    "id": 42691,
                    "name": "Эмоциональная",
                    "slug": "emotsionalnaia",
                    "language": "rus",
                    "games_count": 1583,
                    "image_background": "https://media.rawg.io/media/games/b49/b4912b5dbfc7ed8927b65f05b8507f6c.jpg"
                },
                {
                    "id": 58132,
                    "name": "Атмосферная",
                    "slug": "atmosfernaia",
                    "language": "rus",
                    "games_count": 4619,
                    "image_background": "https://media.rawg.io/media/games/044/044b2ee023930ca138deda151f40c18c.jpg"
                },
                {
                    "id": 58127,
                    "name": "Бой",
                    "slug": "boi-2",
                    "language": "rus",
                    "games_count": 4000,
                    "image_background": "https://media.rawg.io/media/games/e35/e355efef97722d50bec3482a2263b962.jpg"
                },
                {
                    "id": 66533,
                    "name": "Исследования",
                    "slug": "issledovaniia",
                    "language": "rus",
                    "games_count": 4241,
                    "image_background": "https://media.rawg.io/media/games/bde/bdef96f7782fba0ff62dabc37ff4b1f0.jpg"
                },
                {
                    "id": 108,
                    "name": "Mythology",
                    "slug": "mythology",
                    "language": "eng",
                    "games_count": 1684,
                    "image_background": "https://media.rawg.io/media/screenshots/003/003837236ef9419cbb188905836fcfba.jpg"
                },
                {
                    "id": 572,
                    "name": "Emotional",
                    "slug": "emotional",
                    "language": "eng",
                    "games_count": 1704,
                    "image_background": "https://media.rawg.io/media/games/525/525ddc0a9f22c944af01f074e8983ffe.jpg"
                },
                {
                    "id": 42610,
                    "name": "Мифология",
                    "slug": "mifologiia",
                    "language": "rus",
                    "games_count": 624,
                    "image_background": "https://media.rawg.io/media/games/a1f/a1f93b9b287a0808161a35952635867e.jpg"
                },
                {
                    "id": 580,
                    "name": "Souls-like",
                    "slug": "souls-like",
                    "language": "eng",
                    "games_count": 1032,
                    "image_background": "https://media.rawg.io/media/games/043/043f8b4a5d9b767694370d6fbbc8cd3c.jpg"
                },
                {
                    "id": 43374,
                    "name": "Remote Play on TV",
                    "slug": "remote-play-on-tv",
                    "language": "eng",
                    "games_count": 312,
                    "image_background": "https://media.rawg.io/media/games/77c/77ca75b962f0ca9f7de6eb03814d6b5b.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 4397,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 766263,
                    "image": "https://media.rawg.io/media/screenshots/d68/d6868e5f7bce66e326bd48b11ba24b13.jpeg"
                },
                {
                    "id": 766264,
                    "image": "https://media.rawg.io/media/screenshots/928/928cdaf4ae204f202d177bbd65e911b3.jpeg"
                },
                {
                    "id": 766265,
                    "image": "https://media.rawg.io/media/screenshots/a54/a549a06ebe89c570cabb57308c4c42a5.jpeg"
                },
                {
                    "id": 766266,
                    "image": "https://media.rawg.io/media/screenshots/f02/f0279f8199da3e91134078e737e5fbcf.jpg"
                },
                {
                    "id": 766267,
                    "image": "https://media.rawg.io/media/screenshots/e87/e87c57660c7c37fe973c6dd6ebcc1ac6.jpeg"
                },
                {
                    "id": 766268,
                    "image": "https://media.rawg.io/media/screenshots/5b7/5b7280fe437c39d3ce501a867c46a998.jpeg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "it-takes-two-2",
            "name": "It Takes Two",
            "playtime": 10,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2021-03-26",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/d47/d479582ed0a46496ad34f65c7099d7e5.jpg",
            "rating": 4.54,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 719,
                    "percent": 68.48
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 253,
                    "percent": 24.1
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 42,
                    "percent": 4.0
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 36,
                    "percent": 3.43
                }
            ],
            "ratings_count": 1023,
            "reviews_text_count": 19,
            "added": 3841,
            "added_by_status": {
                "yet": 193,
                "owned": 1930,
                "beaten": 898,
                "toplay": 511,
                "dropped": 121,
                "playing": 188
            },
            "metacritic": 88,
            "suggestions_count": 795,
            "updated": "2023-04-16T15:10:38",
            "id": 455597,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 18,
                    "name": "Co-op",
                    "slug": "co-op",
                    "language": "eng",
                    "games_count": 9806,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 411,
                    "name": "cooperative",
                    "slug": "cooperative",
                    "language": "eng",
                    "games_count": 3973,
                    "image_background": "https://media.rawg.io/media/games/baf/baf9905270314e07e6850cffdb51df41.jpg"
                },
                {
                    "id": 9,
                    "name": "Online Co-Op",
                    "slug": "online-co-op",
                    "language": "eng",
                    "games_count": 4246,
                    "image_background": "https://media.rawg.io/media/games/d69/d69810315bd7e226ea2d21f9156af629.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 189,
                    "name": "Female Protagonist",
                    "slug": "female-protagonist",
                    "language": "eng",
                    "games_count": 10677,
                    "image_background": "https://media.rawg.io/media/games/1fb/1fb1c5f7a71d771f440b27ce7f71e7eb.jpg"
                },
                {
                    "id": 42433,
                    "name": "Совместная игра по сети",
                    "slug": "sovmestnaia-igra-po-seti",
                    "language": "rus",
                    "games_count": 1229,
                    "image_background": "https://media.rawg.io/media/games/0bd/0bd5646a3d8ee0ac3314bced91ea306d.jpg"
                },
                {
                    "id": 42464,
                    "name": "Исследование",
                    "slug": "issledovanie",
                    "language": "rus",
                    "games_count": 2990,
                    "image_background": "https://media.rawg.io/media/screenshots/8f0/8f0b94922ad5e59968852649697b2643.jpg"
                },
                {
                    "id": 198,
                    "name": "Split Screen",
                    "slug": "split-screen",
                    "language": "eng",
                    "games_count": 5537,
                    "image_background": "https://media.rawg.io/media/games/27b/27b02ffaab6b250cc31bf43baca1fc34.jpg"
                },
                {
                    "id": 42449,
                    "name": "Локальный мультиплеер",
                    "slug": "lokalnyi-multipleer",
                    "language": "rus",
                    "games_count": 2866,
                    "image_background": "https://media.rawg.io/media/games/270/270b412b66688081497b3d70c100b208.jpg"
                },
                {
                    "id": 75,
                    "name": "Local Co-Op",
                    "slug": "local-co-op",
                    "language": "eng",
                    "games_count": 5032,
                    "image_background": "https://media.rawg.io/media/games/926/926928beb8a9f9b31cf202965aa4cbbc.jpg"
                },
                {
                    "id": 97,
                    "name": "Action RPG",
                    "slug": "action-rpg",
                    "language": "eng",
                    "games_count": 5874,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 42489,
                    "name": "Ролевой экшен",
                    "slug": "rolevoi-ekshen",
                    "language": "rus",
                    "games_count": 2557,
                    "image_background": "https://media.rawg.io/media/games/5be/5bec14622f6faf804a592176577c1347.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5545,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 82,
                    "name": "Magic",
                    "slug": "magic",
                    "language": "eng",
                    "games_count": 8201,
                    "image_background": "https://media.rawg.io/media/games/417/4176298c1b22ccd338ce3dfc34eb7e28.jpg"
                },
                {
                    "id": 406,
                    "name": "Story",
                    "slug": "story",
                    "language": "eng",
                    "games_count": 11617,
                    "image_background": "https://media.rawg.io/media/games/2ee/2eeed8524931b4fae1e4a40d0e5443b5.jpg"
                },
                {
                    "id": 40937,
                    "name": "Steam Trading Cards",
                    "slug": "steam-trading-cards-2",
                    "language": "eng",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 413,
                    "name": "online",
                    "slug": "online",
                    "language": "eng",
                    "games_count": 6655,
                    "image_background": "https://media.rawg.io/media/games/d51/d51ada3b94bfd617bf91d4344ab81ce9.jpg"
                },
                {
                    "id": 42494,
                    "name": "3D-платформер",
                    "slug": "3d-platformer-2",
                    "language": "rus",
                    "games_count": 2558,
                    "image_background": "https://media.rawg.io/media/games/74d/74dafeb9a442b87b9dd4a1d4a2faa37b.jpg"
                },
                {
                    "id": 229,
                    "name": "3D Platformer",
                    "slug": "3d-platformer",
                    "language": "eng",
                    "games_count": 8988,
                    "image_background": "https://media.rawg.io/media/screenshots/57f/57f97397220442e71c51f9ba44b67fec_KzipzFC.jpeg"
                },
                {
                    "id": 42613,
                    "name": "Разделение экрана",
                    "slug": "razdelenie-ekrana",
                    "language": "rus",
                    "games_count": 440,
                    "image_background": "https://media.rawg.io/media/games/1fa/1fa75f0895240b12fc65cc98ae9649fd.jpg"
                },
                {
                    "id": 808,
                    "name": "character",
                    "slug": "character",
                    "language": "eng",
                    "games_count": 9036,
                    "image_background": "https://media.rawg.io/media/games/e11/e11325e2f89151d31f612e38dee3b6a0.jpg"
                },
                {
                    "id": 42691,
                    "name": "Эмоциональная",
                    "slug": "emotsionalnaia",
                    "language": "rus",
                    "games_count": 1583,
                    "image_background": "https://media.rawg.io/media/games/b49/b4912b5dbfc7ed8927b65f05b8507f6c.jpg"
                },
                {
                    "id": 5816,
                    "name": "console",
                    "slug": "console",
                    "language": "eng",
                    "games_count": 1412,
                    "image_background": "https://media.rawg.io/media/games/faa/faa6a4a7a2e57faf2960329630aee211.jpg"
                },
                {
                    "id": 572,
                    "name": "Emotional",
                    "slug": "emotional",
                    "language": "eng",
                    "games_count": 1704,
                    "image_background": "https://media.rawg.io/media/games/525/525ddc0a9f22c944af01f074e8983ffe.jpg"
                },
                {
                    "id": 4565,
                    "name": "offline",
                    "slug": "offline",
                    "language": "eng",
                    "games_count": 1086,
                    "image_background": "https://media.rawg.io/media/games/4fe/4feffcec6315c5f5a96442a8444431ca.jpg"
                },
                {
                    "id": 45201,
                    "name": "Remote Play Together",
                    "slug": "remote-play-together",
                    "language": "eng",
                    "games_count": 1791,
                    "image_background": "https://media.rawg.io/media/games/2a5/2a5072e5b28e1653a10e4f931f1991af.jpg"
                },
                {
                    "id": 46112,
                    "name": "Shared/Split Screen Co-op",
                    "slug": "sharedsplit-screen-co-op",
                    "language": "eng",
                    "games_count": 1164,
                    "image_background": "https://media.rawg.io/media/screenshots/cc0/cc064ab715ba4195ac6d26250218e307.jpg"
                },
                {
                    "id": 42659,
                    "name": "Совместная кампания",
                    "slug": "sovmestnaia-kampaniia",
                    "language": "rus",
                    "games_count": 288,
                    "image_background": "https://media.rawg.io/media/games/a3e/a3ee2e99f5a85e4bd3fc0268ed5fd368.jpg"
                },
                {
                    "id": 59643,
                    "name": "Протагонистка",
                    "slug": "protagonistka",
                    "language": "eng",
                    "games_count": 2760,
                    "image_background": "https://media.rawg.io/media/games/d51/d51ada3b94bfd617bf91d4344ab81ce9.jpg"
                },
                {
                    "id": 1709,
                    "name": "work",
                    "slug": "work",
                    "language": "eng",
                    "games_count": 9597,
                    "image_background": "https://media.rawg.io/media/games/6e3/6e319b00ea9844539b3b20753d8ca0b4.jpg"
                },
                {
                    "id": 163,
                    "name": "Co-op Campaign",
                    "slug": "co-op-campaign",
                    "language": "eng",
                    "games_count": 268,
                    "image_background": "https://media.rawg.io/media/games/70a/70a009eae06ac608b9d8274125e68bb4.jpg"
                },
                {
                    "id": 1652,
                    "name": "night",
                    "slug": "night",
                    "language": "eng",
                    "games_count": 4573,
                    "image_background": "https://media.rawg.io/media/screenshots/d51/d51ac59388da7e8c9a6ad1f52193dfd0.jpg"
                },
                {
                    "id": 42702,
                    "name": "Мини-игры",
                    "slug": "mini-igry",
                    "language": "rus",
                    "games_count": 186,
                    "image_background": "https://media.rawg.io/media/screenshots/366/3669449f2b3b77fc4081a3b7917b2bcb.jpg"
                },
                {
                    "id": 2232,
                    "name": "journey",
                    "slug": "journey",
                    "language": "eng",
                    "games_count": 1920,
                    "image_background": "https://media.rawg.io/media/screenshots/387/3873e4dad2efab0da657e6df50739f5f.jpg"
                },
                {
                    "id": 569,
                    "name": "Minigames",
                    "slug": "minigames",
                    "language": "eng",
                    "games_count": 5894,
                    "image_background": "https://media.rawg.io/media/screenshots/a0e/a0e43f919a9353dc9b376daca5994738.jpg"
                },
                {
                    "id": 892,
                    "name": "love",
                    "slug": "love",
                    "language": "eng",
                    "games_count": 6410,
                    "image_background": "https://media.rawg.io/media/screenshots/92c/92c15660f548971664fdcc66bf15e729.jpg"
                },
                {
                    "id": 3397,
                    "name": "light",
                    "slug": "light",
                    "language": "eng",
                    "games_count": 1782,
                    "image_background": "https://media.rawg.io/media/screenshots/c20/c20b09187629ea6b47d8b3e9132bf839.jpeg"
                },
                {
                    "id": 42658,
                    "name": "Шахты",
                    "slug": "shakhty",
                    "language": "rus",
                    "games_count": 295,
                    "image_background": "https://media.rawg.io/media/screenshots/436/436209118fd9fc8dbc3942dcc5373834.jpg"
                },
                {
                    "id": 316,
                    "name": "Mining",
                    "slug": "mining",
                    "language": "eng",
                    "games_count": 928,
                    "image_background": "https://media.rawg.io/media/screenshots/671/671da72d282b3169568748fc2fcec927.jpg"
                },
                {
                    "id": 3626,
                    "name": "treasure",
                    "slug": "treasure",
                    "language": "eng",
                    "games_count": 1889,
                    "image_background": "https://media.rawg.io/media/screenshots/082/08204cebaa6276237d4ac940d3aea52d.jpg"
                },
                {
                    "id": 688,
                    "name": "relationship",
                    "slug": "relationship",
                    "language": "eng",
                    "games_count": 1038,
                    "image_background": "https://media.rawg.io/media/games/557/557303d2e44105033f15011fd26ad4fd.jpg"
                },
                {
                    "id": 2774,
                    "name": "learn",
                    "slug": "learn",
                    "language": "eng",
                    "games_count": 1353,
                    "image_background": "https://media.rawg.io/media/games/313/3137f0b7fb36b53e34abcde6e7607909.jpg"
                },
                {
                    "id": 4451,
                    "name": "obstacles",
                    "slug": "obstacles",
                    "language": "eng",
                    "games_count": 2248,
                    "image_background": "https://media.rawg.io/media/screenshots/fad/fad027fba95ef5d9f8e2ff0b86d6c9bf.jpg"
                },
                {
                    "id": 2353,
                    "name": "delivery",
                    "slug": "delivery",
                    "language": "eng",
                    "games_count": 291,
                    "image_background": "https://media.rawg.io/media/screenshots/f7a/f7af8c0fc22975f59935f398b615e359.jpg"
                }
            ],
            "esrb_rating": {
                "id": 2,
                "name": "Everyone 10+",
                "slug": "everyone-10-plus",
                "name_en": "Everyone 10+",
                "name_ru": "С 10 лет"
            },
            "user_game": None,
            "reviews_count": 1050,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/d47/d479582ed0a46496ad34f65c7099d7e5.jpg"
                },
                {
                    "id": 2634032,
                    "image": "https://media.rawg.io/media/screenshots/252/252844a85405a3147440806709a47f79.jpg"
                },
                {
                    "id": 2634033,
                    "image": "https://media.rawg.io/media/screenshots/88a/88a0a4d7a1f4dbe78c2c34810afcaffa.jpg"
                },
                {
                    "id": 2634034,
                    "image": "https://media.rawg.io/media/screenshots/bef/bef5d6085129fda4d26a2293b9edb30e.jpg"
                },
                {
                    "id": 2769287,
                    "image": "https://media.rawg.io/media/screenshots/0f1/0f157efb373e3c5da268f2ecdb03701e.jpg"
                },
                {
                    "id": 2769288,
                    "image": "https://media.rawg.io/media/screenshots/5f4/5f429ee02d86be1822963fd0a77a71ab.jpg"
                },
                {
                    "id": 2769289,
                    "image": "https://media.rawg.io/media/screenshots/c01/c01d8a0c413b3a065ea52b80f1ad6212.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "splatoon-3",
            "name": "Splatoon 3",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2022-09-09",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/360/360ac0a839ab0f0d9a70b35d38264cb0.jpg",
            "rating": 4.5,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 17,
                    "percent": 56.67
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 11,
                    "percent": 36.67
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 2,
                    "percent": 6.67
                }
            ],
            "ratings_count": 29,
            "reviews_text_count": 1,
            "added": 130,
            "added_by_status": {
                "yet": 10,
                "owned": 20,
                "beaten": 15,
                "toplay": 49,
                "dropped": 9,
                "playing": 27
            },
            "metacritic": 83,
            "suggestions_count": 282,
            "updated": "2023-04-09T18:31:59",
            "id": 558975,
            "score": None,
            "clip": None,
            "tags": [],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 30,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/360/360ac0a839ab0f0d9a70b35d38264cb0.jpg"
                },
                {
                    "id": 2717657,
                    "image": "https://media.rawg.io/media/screenshots/52a/52ab56f49dacec085803b93e20cde2d8.jpg"
                },
                {
                    "id": 2717658,
                    "image": "https://media.rawg.io/media/screenshots/4ef/4ef5d976b974873c574126ed3e081f99.jpg"
                },
                {
                    "id": 2717659,
                    "image": "https://media.rawg.io/media/screenshots/3eb/3eb910c77a5597197276f3ea541916d2.jpg"
                },
                {
                    "id": 2717660,
                    "image": "https://media.rawg.io/media/screenshots/3ea/3eadccae65f82027a0e0ddc1f4ea5d52.jpg"
                },
                {
                    "id": 2717661,
                    "image": "https://media.rawg.io/media/screenshots/ea6/ea669a514a8fdd905b5d67384561014b.jpg"
                },
                {
                    "id": 2717662,
                    "image": "https://media.rawg.io/media/screenshots/441/44158afb4810a7141760dc3b03d143ba.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 2,
                    "name": "Shooter",
                    "slug": "shooter"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "resident-evil-2-2019",
            "name": "Resident Evil 2",
            "playtime": 11,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2019-01-25",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/053/053fc543bf488349610f1ae2d0c1b51b.jpg",
            "rating": 4.48,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 1195,
                    "percent": 62.89
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 557,
                    "percent": 29.32
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 83,
                    "percent": 4.37
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 65,
                    "percent": 3.42
                }
            ],
            "ratings_count": 1878,
            "reviews_text_count": 20,
            "added": 4683,
            "added_by_status": {
                "yet": 367,
                "owned": 1414,
                "beaten": 1651,
                "toplay": 866,
                "dropped": 236,
                "playing": 149
            },
            "metacritic": 91,
            "suggestions_count": 502,
            "updated": "2023-04-16T20:36:04",
            "id": 58813,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42428,
                    "name": "Шутер",
                    "slug": "shuter",
                    "language": "rus",
                    "games_count": 6479,
                    "image_background": "https://media.rawg.io/media/games/c24/c24ec439abf4a2e92f3429dfa83f7f94.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 42465,
                    "name": "Головоломка",
                    "slug": "golovolomka",
                    "language": "rus",
                    "games_count": 11084,
                    "image_background": "https://media.rawg.io/media/games/021/021c4e21a1824d2526f925eff6324653.jpg"
                },
                {
                    "id": 42420,
                    "name": "Сложная",
                    "slug": "slozhnaia",
                    "language": "rus",
                    "games_count": 4385,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 42461,
                    "name": "Классика",
                    "slug": "klassika",
                    "language": "rus",
                    "games_count": 1391,
                    "image_background": "https://media.rawg.io/media/games/bc0/bc06a29ceac58652b684deefe7d56099.jpg"
                },
                {
                    "id": 42491,
                    "name": "Мясо",
                    "slug": "miaso",
                    "language": "rus",
                    "games_count": 3850,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 26,
                    "name": "Gore",
                    "slug": "gore",
                    "language": "eng",
                    "games_count": 5083,
                    "image_background": "https://media.rawg.io/media/games/998/9980c4296f311d8bcc5b451ca51e4fe1.jpg"
                },
                {
                    "id": 193,
                    "name": "Classic",
                    "slug": "classic",
                    "language": "eng",
                    "games_count": 1767,
                    "image_background": "https://media.rawg.io/media/games/14a/14a83c56ff668baaced6e8c8704b6391.jpg"
                },
                {
                    "id": 1,
                    "name": "Survival",
                    "slug": "survival",
                    "language": "eng",
                    "games_count": 7130,
                    "image_background": "https://media.rawg.io/media/games/d7d/d7d33daa1892e2468cd0263d5dfc957e.jpg"
                },
                {
                    "id": 42452,
                    "name": "Выживание",
                    "slug": "vyzhivanie",
                    "language": "rus",
                    "games_count": 4550,
                    "image_background": "https://media.rawg.io/media/games/daa/daaee07fcb40744d90cf8142f94a241f.jpg"
                },
                {
                    "id": 42404,
                    "name": "Женщина-протагонист",
                    "slug": "zhenshchina-protagonist",
                    "language": "rus",
                    "games_count": 2416,
                    "image_background": "https://media.rawg.io/media/games/7f6/7f6cd70ba2ad57053b4847c13569f2d8.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42477,
                    "name": "Мрачная",
                    "slug": "mrachnaia",
                    "language": "rus",
                    "games_count": 3416,
                    "image_background": "https://media.rawg.io/media/games/d9f/d9f982e042df6263684ba1fdea3efc1c.jpg"
                },
                {
                    "id": 41,
                    "name": "Dark",
                    "slug": "dark",
                    "language": "eng",
                    "games_count": 14620,
                    "image_background": "https://media.rawg.io/media/games/ffe/ffed87105b14f5beff72ff44a7793fd5.jpg"
                },
                {
                    "id": 63,
                    "name": "Zombies",
                    "slug": "zombies",
                    "language": "eng",
                    "games_count": 10130,
                    "image_background": "https://media.rawg.io/media/games/d64/d646810b629081cc12aec49ed9f49441.jpg"
                },
                {
                    "id": 42544,
                    "name": "Зомби",
                    "slug": "zombi-2",
                    "language": "rus",
                    "games_count": 1929,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42471,
                    "name": "Хоррор на выживание",
                    "slug": "khorror-na-vyzhivanie",
                    "language": "rus",
                    "games_count": 2127,
                    "image_background": "https://media.rawg.io/media/games/447/4470c1e76f01acfaf5af9c207d1c1c92.jpg"
                },
                {
                    "id": 17,
                    "name": "Survival Horror",
                    "slug": "survival-horror",
                    "language": "eng",
                    "games_count": 8163,
                    "image_background": "https://media.rawg.io/media/games/b54/b54598d1d5cc31899f4f0a7e3122a7b0.jpg"
                },
                {
                    "id": 42466,
                    "name": "Римейк",
                    "slug": "rimeik",
                    "language": "rus",
                    "games_count": 206,
                    "image_background": "https://media.rawg.io/media/games/8fc/8fc59e74133fd8a8a436b7e2d0fb36c2.jpg"
                },
                {
                    "id": 271,
                    "name": "Remake",
                    "slug": "remake",
                    "language": "eng",
                    "games_count": 1767,
                    "image_background": "https://media.rawg.io/media/games/7a4/7a45e4cdc5b07f316d49cf147b083b27.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 86,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 270,
                    "name": "Blood",
                    "slug": "blood",
                    "language": "eng",
                    "games_count": 1984,
                    "image_background": "https://media.rawg.io/media/games/63f/63f0e68688cad279ed38cde931dbfcdb.jpg"
                },
                {
                    "id": 285,
                    "name": "Psychological",
                    "slug": "psychological",
                    "language": "eng",
                    "games_count": 1068,
                    "image_background": "https://media.rawg.io/media/games/fae/faebf3c8cbf30db3f46bfbecf6ada3d6.jpg"
                },
                {
                    "id": 62348,
                    "name": "first person mod",
                    "slug": "first-person-mod",
                    "language": "eng",
                    "games_count": 15,
                    "image_background": "https://media.rawg.io/media/games/e3d/e3ddc524c6292a435d01d97cc5f42ea7.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 1900,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/053/053fc543bf488349610f1ae2d0c1b51b.jpg"
                },
                {
                    "id": 837286,
                    "image": "https://media.rawg.io/media/screenshots/9e6/9e6e83b37dfd176eab77a829c5c7a109.jpg"
                },
                {
                    "id": 837287,
                    "image": "https://media.rawg.io/media/screenshots/ca6/ca6629a8a4565b8ae7816ffcb4d38657.jpg"
                },
                {
                    "id": 837288,
                    "image": "https://media.rawg.io/media/screenshots/df4/df450d260b14fb77ac238d77fe98746d.jpg"
                },
                {
                    "id": 837289,
                    "image": "https://media.rawg.io/media/screenshots/fac/facb42731a6cc48e8fdfaef995f3ed71.jpg"
                },
                {
                    "id": 837290,
                    "image": "https://media.rawg.io/media/screenshots/4bf/4bf2b3c6822715ec3b01882e0cf97572.jpg"
                },
                {
                    "id": 837291,
                    "image": "https://media.rawg.io/media/screenshots/bdb/bdbf60136aad78a718679d2f1ac317f9.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 2,
                    "name": "Shooter",
                    "slug": "shooter"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "ori-and-the-will-of-the-wisps",
            "name": "Ori and the Will of the Wisps",
            "playtime": 11,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2020-03-10",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/718/71891d2484a592d871e91dc826707e1c.jpg",
            "rating": 4.47,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 693,
                    "percent": 64.41
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 277,
                    "percent": 25.74
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 65,
                    "percent": 6.04
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 41,
                    "percent": 3.81
                }
            ],
            "ratings_count": 1056,
            "reviews_text_count": 12,
            "added": 5376,
            "added_by_status": {
                "yet": 483,
                "owned": 2865,
                "beaten": 828,
                "toplay": 904,
                "dropped": 177,
                "playing": 119
            },
            "metacritic": 91,
            "suggestions_count": 414,
            "updated": "2023-04-16T07:20:31",
            "id": 28199,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42442,
                    "name": "Открытый мир",
                    "slug": "otkrytyi-mir",
                    "language": "rus",
                    "games_count": 4297,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42435,
                    "name": "Шедевр",
                    "slug": "shedevr",
                    "language": "rus",
                    "games_count": 1059,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 42465,
                    "name": "Головоломка",
                    "slug": "golovolomka",
                    "language": "rus",
                    "games_count": 11084,
                    "image_background": "https://media.rawg.io/media/games/021/021c4e21a1824d2526f925eff6324653.jpg"
                },
                {
                    "id": 42420,
                    "name": "Сложная",
                    "slug": "slozhnaia",
                    "language": "rus",
                    "games_count": 4385,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 42480,
                    "name": "Фэнтези",
                    "slug": "fentezi",
                    "language": "rus",
                    "games_count": 7813,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 64,
                    "name": "Fantasy",
                    "slug": "fantasy",
                    "language": "eng",
                    "games_count": 25175,
                    "image_background": "https://media.rawg.io/media/games/33d/33df5a032898b8ab7e3773c7a5f1d336.jpg"
                },
                {
                    "id": 49,
                    "name": "Difficult",
                    "slug": "difficult",
                    "language": "eng",
                    "games_count": 13060,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 42463,
                    "name": "Платформер",
                    "slug": "platformer-2",
                    "language": "rus",
                    "games_count": 6297,
                    "image_background": "https://media.rawg.io/media/games/89a/89a700d3c6a76bd0610ca89ccd20da54.jpg"
                },
                {
                    "id": 42464,
                    "name": "Исследование",
                    "slug": "issledovanie",
                    "language": "rus",
                    "games_count": 2990,
                    "image_background": "https://media.rawg.io/media/screenshots/8f0/8f0b94922ad5e59968852649697b2643.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42586,
                    "name": "Милая",
                    "slug": "milaia",
                    "language": "rus",
                    "games_count": 8056,
                    "image_background": "https://media.rawg.io/media/games/594/59487800889ebac294c7c2c070d02356.jpg"
                },
                {
                    "id": 88,
                    "name": "Cute",
                    "slug": "cute",
                    "language": "eng",
                    "games_count": 30059,
                    "image_background": "https://media.rawg.io/media/games/51c/51c430f1795c79b78f863a9f22dc422d.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5545,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 42690,
                    "name": "Красивая",
                    "slug": "krasivaia",
                    "language": "rus",
                    "games_count": 537,
                    "image_background": "https://media.rawg.io/media/games/90c/90caf1fcb836cad70013452f6f239008.jpg"
                },
                {
                    "id": 259,
                    "name": "Metroidvania",
                    "slug": "metroidvania",
                    "language": "eng",
                    "games_count": 4166,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcb1c529c764700d55f3bbc1b0fbb5b.jpg"
                },
                {
                    "id": 42462,
                    "name": "Метроидвания",
                    "slug": "metroidvaniia",
                    "language": "rus",
                    "games_count": 899,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 83,
                    "name": "Puzzle-Platformer",
                    "slug": "puzzle-platformer",
                    "language": "eng",
                    "games_count": 9984,
                    "image_background": "https://media.rawg.io/media/screenshots/2e0/2e0fcc99cdc363288ab3312877bb8444.jpg"
                },
                {
                    "id": 42592,
                    "name": "Похожа на Dark Souls",
                    "slug": "pokhozha-na-dark-souls",
                    "language": "rus",
                    "games_count": 605,
                    "image_background": "https://media.rawg.io/media/games/718/71891d2484a592d871e91dc826707e1c.jpg"
                },
                {
                    "id": 42691,
                    "name": "Эмоциональная",
                    "slug": "emotsionalnaia",
                    "language": "rus",
                    "games_count": 1583,
                    "image_background": "https://media.rawg.io/media/games/b49/b4912b5dbfc7ed8927b65f05b8507f6c.jpg"
                },
                {
                    "id": 578,
                    "name": "Masterpiece",
                    "slug": "masterpiece",
                    "language": "eng",
                    "games_count": 276,
                    "image_background": "https://media.rawg.io/media/games/0fa/0fa9e2b8397b332902d3b56c73888d52.jpg"
                },
                {
                    "id": 577,
                    "name": "Beautiful",
                    "slug": "beautiful",
                    "language": "eng",
                    "games_count": 1820,
                    "image_background": "https://media.rawg.io/media/games/d3e/d3ee2d7653cf9d4640335ff7a471ab07.jpg"
                },
                {
                    "id": 572,
                    "name": "Emotional",
                    "slug": "emotional",
                    "language": "eng",
                    "games_count": 1704,
                    "image_background": "https://media.rawg.io/media/games/525/525ddc0a9f22c944af01f074e8983ffe.jpg"
                },
                {
                    "id": 580,
                    "name": "Souls-like",
                    "slug": "souls-like",
                    "language": "eng",
                    "games_count": 1032,
                    "image_background": "https://media.rawg.io/media/games/043/043f8b4a5d9b767694370d6fbbc8cd3c.jpg"
                }
            ],
            "esrb_rating": {
                "id": 1,
                "name": "Everyone",
                "slug": "everyone",
                "name_en": "Everyone",
                "name_ru": "Для всех"
            },
            "user_game": None,
            "reviews_count": 1076,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/718/71891d2484a592d871e91dc826707e1c.jpg"
                },
                {
                    "id": 269737,
                    "image": "https://media.rawg.io/media/screenshots/85d/85dcab4cda43f9b04a7c266d888b0d2a.jpeg"
                },
                {
                    "id": 269738,
                    "image": "https://media.rawg.io/media/screenshots/787/78717a4bd40ff4490bf779903c999807.jpeg"
                },
                {
                    "id": 269739,
                    "image": "https://media.rawg.io/media/screenshots/943/943907c512a780b1a4db86cef846ee37.jpeg"
                },
                {
                    "id": 778837,
                    "image": "https://media.rawg.io/media/screenshots/1d6/1d692afa0ccd7a5741a5a85859155dfb.jpg"
                },
                {
                    "id": 778838,
                    "image": "https://media.rawg.io/media/screenshots/3d1/3d15ad60c52476284fa6ca6a276ba280.jpg"
                },
                {
                    "id": 778839,
                    "image": "https://media.rawg.io/media/screenshots/fe0/fe0f31e9e413d2a35df07159916e909d.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "marvels-spider-man",
            "name": "Marvel's Spider-Man",
            "playtime": 6,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2018-09-07",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg",
            "rating": 4.46,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 1934,
                    "percent": 58.87
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 1082,
                    "percent": 32.94
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 190,
                    "percent": 5.78
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 79,
                    "percent": 2.4
                }
            ],
            "ratings_count": 3222,
            "reviews_text_count": 50,
            "added": 9217,
            "added_by_status": {
                "yet": 334,
                "owned": 4625,
                "beaten": 2890,
                "toplay": 910,
                "dropped": 185,
                "playing": 273
            },
            "metacritic": 87,
            "suggestions_count": 549,
            "updated": "2023-04-16T07:21:22",
            "id": 58134,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 110,
                    "name": "Cinematic",
                    "slug": "cinematic",
                    "language": "eng",
                    "games_count": 1313,
                    "image_background": "https://media.rawg.io/media/games/7ac/7aca7ccf0e70cd0974cb899ab9e5158e.jpg"
                },
                {
                    "id": 203,
                    "name": "Beat 'em up",
                    "slug": "beat-em-up",
                    "language": "eng",
                    "games_count": 2747,
                    "image_background": "https://media.rawg.io/media/games/c40/c40f9f0a3d1b4601a7a44d230c95f126.jpg"
                },
                {
                    "id": 37797,
                    "name": "true exclusive",
                    "slug": "true-exclusive",
                    "language": "eng",
                    "games_count": 3995,
                    "image_background": "https://media.rawg.io/media/games/214/214b29aeff13a0ae6a70fc4426e85991.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 86,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 268,
                    "name": "Comic Book",
                    "slug": "comic-book",
                    "language": "eng",
                    "games_count": 820,
                    "image_background": "https://media.rawg.io/media/games/048/048b46cdc66cbc7e235e1f359c2a77ec.jpg"
                },
                {
                    "id": 234,
                    "name": "Superhero",
                    "slug": "superhero",
                    "language": "eng",
                    "games_count": 1268,
                    "image_background": "https://media.rawg.io/media/games/d2e/d2ee15fda80056efef174da4ca5ae54f.jpg"
                },
                {
                    "id": 78,
                    "name": "America",
                    "slug": "america",
                    "language": "eng",
                    "games_count": 440,
                    "image_background": "https://media.rawg.io/media/games/4c2/4c23c4a88f53e7e482d72ddfcf5b9b41.jpg"
                },
                {
                    "id": 43369,
                    "name": "new york",
                    "slug": "new-york-2",
                    "language": "eng",
                    "games_count": 2,
                    "image_background": "https://media.rawg.io/media/screenshots/e3c/e3cc9dcd0d4779fcdc08a01d150ea7f9.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 3285,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 1325929,
                    "image": "https://media.rawg.io/media/screenshots/331/331ba5164c5c53a5d59aad3fe9771ac7.jpg"
                },
                {
                    "id": 1325930,
                    "image": "https://media.rawg.io/media/screenshots/a15/a15b42bd8a652a3733c6ad419ebb24bd.jpg"
                },
                {
                    "id": 1325931,
                    "image": "https://media.rawg.io/media/screenshots/150/150589c127b28f287f992c2bd426b443.jpg"
                },
                {
                    "id": 1325932,
                    "image": "https://media.rawg.io/media/screenshots/f52/f526988f895b554dccf68767557a8518.jpg"
                },
                {
                    "id": 1325958,
                    "image": "https://media.rawg.io/media/screenshots/745/74589db2dee21101d7af690976fca902.jpg"
                },
                {
                    "id": 1325959,
                    "image": "https://media.rawg.io/media/screenshots/090/09063845f2efe6d0b9bc908e2652c1e1.jpeg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "hades-2018",
            "name": "Hades",
            "playtime": 9,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                },
                {
                    "store": {
                        "id": 11,
                        "name": "Epic Games",
                        "slug": "epic-games"
                    }
                }
            ],
            "released": "2020-09-17",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/1f4/1f47a270b8f241e4676b14d39ec620f7.jpg",
            "rating": 4.46,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 991,
                    "percent": 62.21
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 446,
                    "percent": 28.0
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 106,
                    "percent": 6.65
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 50,
                    "percent": 3.14
                }
            ],
            "ratings_count": 1558,
            "reviews_text_count": 27,
            "added": 7111,
            "added_by_status": {
                "yet": 401,
                "owned": 4166,
                "beaten": 992,
                "toplay": 644,
                "dropped": 463,
                "playing": 445
            },
            "metacritic": 93,
            "suggestions_count": 576,
            "updated": "2023-04-16T07:21:08",
            "id": 274755,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 24,
                    "name": "RPG",
                    "slug": "rpg",
                    "language": "eng",
                    "games_count": 17009,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 42412,
                    "name": "Ролевая игра",
                    "slug": "rolevaia-igra",
                    "language": "rus",
                    "games_count": 13302,
                    "image_background": "https://media.rawg.io/media/games/ee3/ee3e10193aafc3230ba1cae426967d10.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 45,
                    "name": "2D",
                    "slug": "2d",
                    "language": "eng",
                    "games_count": 200870,
                    "image_background": "https://media.rawg.io/media/games/f46/f466571d536f2e3ea9e815ad17177501.jpg"
                },
                {
                    "id": 64,
                    "name": "Fantasy",
                    "slug": "fantasy",
                    "language": "eng",
                    "games_count": 25175,
                    "image_background": "https://media.rawg.io/media/games/33d/33df5a032898b8ab7e3773c7a5f1d336.jpg"
                },
                {
                    "id": 97,
                    "name": "Action RPG",
                    "slug": "action-rpg",
                    "language": "eng",
                    "games_count": 5874,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 42489,
                    "name": "Ролевой экшен",
                    "slug": "rolevoi-ekshen",
                    "language": "rus",
                    "games_count": 2557,
                    "image_background": "https://media.rawg.io/media/games/5be/5bec14622f6faf804a592176577c1347.jpg"
                },
                {
                    "id": 42411,
                    "name": "Ранний доступ",
                    "slug": "rannii-dostup",
                    "language": "rus",
                    "games_count": 11500,
                    "image_background": "https://media.rawg.io/media/screenshots/88b/88b5f27f07d6ca2f8a3cd0b36e03a670.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 14,
                    "name": "Early Access",
                    "slug": "early-access",
                    "language": "eng",
                    "games_count": 11980,
                    "image_background": "https://media.rawg.io/media/games/009/009e4e84975d6a60173ec1199db25aa3.jpg"
                },
                {
                    "id": 42487,
                    "name": "Слэшер",
                    "slug": "slesher",
                    "language": "rus",
                    "games_count": 1862,
                    "image_background": "https://media.rawg.io/media/games/21a/21ad672cedee9b4378abb6c2d2e626ee.jpg"
                },
                {
                    "id": 68,
                    "name": "Hack and Slash",
                    "slug": "hack-and-slash",
                    "language": "eng",
                    "games_count": 3414,
                    "image_background": "https://media.rawg.io/media/games/af7/af7a831001c5c32c46e950cc883b8cb7.jpg"
                },
                {
                    "id": 42520,
                    "name": "Реиграбельность",
                    "slug": "reigrabelnost",
                    "language": "rus",
                    "games_count": 1803,
                    "image_background": "https://media.rawg.io/media/games/10d/10d19e52e5e8415d16a4d344fe711874.jpg"
                },
                {
                    "id": 5,
                    "name": "Replay Value",
                    "slug": "replay-value",
                    "language": "eng",
                    "games_count": 1253,
                    "image_background": "https://media.rawg.io/media/games/10d/10d19e52e5e8415d16a4d344fe711874.jpg"
                },
                {
                    "id": 42419,
                    "name": "Рогалик",
                    "slug": "rogalik",
                    "language": "rus",
                    "games_count": 2639,
                    "image_background": "https://media.rawg.io/media/games/dd5/dd50d4266915d56dd5b63ae1bf72606a.jpg"
                },
                {
                    "id": 99,
                    "name": "Isometric",
                    "slug": "isometric",
                    "language": "eng",
                    "games_count": 3960,
                    "image_background": "https://media.rawg.io/media/games/032/0329db96e252aa41e672da2ba16f914c.jpg"
                },
                {
                    "id": 639,
                    "name": "Roguelike",
                    "slug": "roguelike",
                    "language": "eng",
                    "games_count": 11646,
                    "image_background": "https://media.rawg.io/media/games/fad/fadc4be043ed07904012d47cd02671e4.jpg"
                },
                {
                    "id": 42591,
                    "name": "Упрощённый рогалик",
                    "slug": "uproshchionnyi-rogalik",
                    "language": "rus",
                    "games_count": 2169,
                    "image_background": "https://media.rawg.io/media/games/434/43431e04f0cd5419a3d8e31a5c8c3d5d.jpg"
                },
                {
                    "id": 640,
                    "name": "Roguelite",
                    "slug": "roguelite",
                    "language": "eng",
                    "games_count": 5137,
                    "image_background": "https://media.rawg.io/media/games/5f4/5f4780690dbf04900cbac5f05b9305f3.jpg"
                },
                {
                    "id": 48,
                    "name": "Dungeon Crawler",
                    "slug": "dungeon-crawler",
                    "language": "eng",
                    "games_count": 6326,
                    "image_background": "https://media.rawg.io/media/games/b17/b175178f8842276b8b18b339fe3146a1.jpg"
                },
                {
                    "id": 42483,
                    "name": "Рисованная графика",
                    "slug": "risovannaia-grafika",
                    "language": "rus",
                    "games_count": 2655,
                    "image_background": "https://media.rawg.io/media/screenshots/332/3327c47e0abc76882fc96c434d2e06bd.jpg"
                },
                {
                    "id": 258,
                    "name": "Hand-drawn",
                    "slug": "hand-drawn",
                    "language": "eng",
                    "games_count": 5696,
                    "image_background": "https://media.rawg.io/media/screenshots/5a3/5a36930b16d9b1949d8c8c92b5a28d89.jpg"
                },
                {
                    "id": 42593,
                    "name": "Одна жизнь",
                    "slug": "odna-zhizn",
                    "language": "rus",
                    "games_count": 1115,
                    "image_background": "https://media.rawg.io/media/games/f3e/f3eec35c6218dcfd93a537751e6bfa61.jpg"
                },
                {
                    "id": 124,
                    "name": "Perma Death",
                    "slug": "perma-death",
                    "language": "eng",
                    "games_count": 1671,
                    "image_background": "https://media.rawg.io/media/screenshots/67e/67ed02eae8de073929c3d0809f60c65b.jpg"
                },
                {
                    "id": 3383,
                    "name": "dungeons",
                    "slug": "dungeons",
                    "language": "eng",
                    "games_count": 43,
                    "image_background": "https://media.rawg.io/media/screenshots/ff8/ff8a1b6a074ec09d0dbce53f2d529d31.jpg"
                }
            ],
            "esrb_rating": {
                "id": 6,
                "name": "Rating Pending",
                "slug": "rating-pending",
                "name_en": "Rating Pending",
                "name_ru": "Рейтинг обсуждается"
            },
            "user_game": None,
            "reviews_count": 1593,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/1f4/1f47a270b8f241e4676b14d39ec620f7.jpg"
                },
                {
                    "id": 1767940,
                    "image": "https://media.rawg.io/media/screenshots/546/546826ed2cde2dec94e1b470c8cbb9ac.jpg"
                },
                {
                    "id": 1767941,
                    "image": "https://media.rawg.io/media/screenshots/0aa/0aa5e778c3cf8f47e3ee7f8e0185eb16.jpg"
                },
                {
                    "id": 1767942,
                    "image": "https://media.rawg.io/media/screenshots/a06/a0649473a36bb879cef146a244d9cb54.jpg"
                },
                {
                    "id": 1767943,
                    "image": "https://media.rawg.io/media/screenshots/f70/f7079ac3e96a5da13c8cfda6fb9fe249.jpg"
                },
                {
                    "id": 1767944,
                    "image": "https://media.rawg.io/media/screenshots/8d4/8d4d9c4ffe01ad0addc29353a895d562.jpg"
                },
                {
                    "id": 1853036,
                    "image": "https://media.rawg.io/media/screenshots/ece/eceaae77766d7f7b0fdfa4f3bb4eff98.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "ghost-of-tsushima",
            "name": "Ghost of Tsushima",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2020-07-17",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/f24/f2493ea338fe7bd3c7d73750a85a0959.jpeg",
            "rating": 4.46,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 524,
                    "percent": 61.65
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 247,
                    "percent": 29.06
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 52,
                    "percent": 6.12
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 27,
                    "percent": 3.18
                }
            ],
            "ratings_count": 825,
            "reviews_text_count": 16,
            "added": 5030,
            "added_by_status": {
                "yet": 310,
                "owned": 2678,
                "beaten": 704,
                "toplay": 1098,
                "dropped": 96,
                "playing": 144
            },
            "metacritic": 83,
            "suggestions_count": 434,
            "updated": "2023-04-16T17:35:29",
            "id": 58550,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 24,
                    "name": "RPG",
                    "slug": "rpg",
                    "language": "eng",
                    "games_count": 17009,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 1752,
                    "name": "japanese",
                    "slug": "japanese",
                    "language": "eng",
                    "games_count": 419,
                    "image_background": "https://media.rawg.io/media/screenshots/677/67704185591ed102ac690a2a67468a6d.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 850,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/f24/f2493ea338fe7bd3c7d73750a85a0959.jpeg"
                },
                {
                    "id": 777610,
                    "image": "https://media.rawg.io/media/screenshots/2e7/2e7a9e16cae5ba5daca74029981029c3.jpg"
                },
                {
                    "id": 777611,
                    "image": "https://media.rawg.io/media/screenshots/ba0/ba09edd0dc18e56a3b62aba32b9c3ed6.jpg"
                },
                {
                    "id": 777612,
                    "image": "https://media.rawg.io/media/screenshots/7a6/7a6d792781b4ee1414cdb0649a2e56ac.jpg"
                },
                {
                    "id": 777613,
                    "image": "https://media.rawg.io/media/screenshots/aa5/aa543c81d5f342a7d3aecc55df89f66e.jpg"
                },
                {
                    "id": 777614,
                    "image": "https://media.rawg.io/media/screenshots/547/5476a303d0ec920c29264ff18da5741a.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "judgment-2",
            "name": "Judgment",
            "playtime": 7,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2018-12-13",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/338/33848ebb15683ea022c08f39f01b810f.jpg",
            "rating": 4.44,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 36,
                    "percent": 58.06
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 19,
                    "percent": 30.65
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 6,
                    "percent": 9.68
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 1,
                    "percent": 1.61
                }
            ],
            "ratings_count": 59,
            "reviews_text_count": 2,
            "added": 733,
            "added_by_status": {
                "yet": 36,
                "owned": 559,
                "beaten": 55,
                "toplay": 51,
                "dropped": 16,
                "playing": 16
            },
            "metacritic": 82,
            "suggestions_count": 146,
            "updated": "2023-03-28T15:14:36",
            "id": 630676,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 212947,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31248,
                    "image_background": "https://media.rawg.io/media/games/4a0/4a0a1316102366260e6f38fd2a9cfdce.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29187,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29723,
                    "image_background": "https://media.rawg.io/media/games/120/1201a40e4364557b124392ee50317b99.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13953,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13723,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9464,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4662,
                    "image_background": "https://media.rawg.io/media/games/e2d/e2d3f396b16dded0f841c17c9799a882.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13748,
                    "image_background": "https://media.rawg.io/media/games/e1f/e1ffbeb1bac25b19749ad285ca29e158.jpg"
                },
                {
                    "id": 42477,
                    "name": "Мрачная",
                    "slug": "mrachnaia",
                    "language": "rus",
                    "games_count": 3396,
                    "image_background": "https://media.rawg.io/media/games/b49/b4912b5dbfc7ed8927b65f05b8507f6c.jpg"
                },
                {
                    "id": 41,
                    "name": "Dark",
                    "slug": "dark",
                    "language": "eng",
                    "games_count": 14525,
                    "image_background": "https://media.rawg.io/media/games/120/1201a40e4364557b124392ee50317b99.jpg"
                },
                {
                    "id": 42487,
                    "name": "Слэшер",
                    "slug": "slesher",
                    "language": "rus",
                    "games_count": 1850,
                    "image_background": "https://media.rawg.io/media/games/5be/5bec14622f6faf804a592176577c1347.jpg"
                },
                {
                    "id": 68,
                    "name": "Hack and Slash",
                    "slug": "hack-and-slash",
                    "language": "eng",
                    "games_count": 3397,
                    "image_background": "https://media.rawg.io/media/games/d0f/d0f91fe1d92332147e5db74e207cfc7a.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5501,
                    "image_background": "https://media.rawg.io/media/games/a79/a79d2fc90c4dbf07a8580b19600fd61d.jpg"
                },
                {
                    "id": 42460,
                    "name": "Реализм",
                    "slug": "realizm",
                    "language": "rus",
                    "games_count": 3598,
                    "image_background": "https://media.rawg.io/media/games/78d/78dfae12fb8c5b16cd78648553071e0a.jpg"
                },
                {
                    "id": 110,
                    "name": "Cinematic",
                    "slug": "cinematic",
                    "language": "eng",
                    "games_count": 1307,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 77,
                    "name": "Realistic",
                    "slug": "realistic",
                    "language": "eng",
                    "games_count": 3635,
                    "image_background": "https://media.rawg.io/media/games/25c/25c4776ab5723d5d735d8bf617ca12d9.jpg"
                },
                {
                    "id": 203,
                    "name": "Beat 'em up",
                    "slug": "beat-em-up",
                    "language": "eng",
                    "games_count": 2742,
                    "image_background": "https://media.rawg.io/media/games/416/4164ca654a339af5be8e63cc9c480c70.jpg"
                },
                {
                    "id": 144,
                    "name": "Crime",
                    "slug": "crime",
                    "language": "eng",
                    "games_count": 2572,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 571,
                    "name": "3D",
                    "slug": "3d",
                    "language": "eng",
                    "games_count": 81491,
                    "image_background": "https://media.rawg.io/media/games/cb4/cb487ab3c54b81cb685388bab42ec848.jpeg"
                },
                {
                    "id": 42443,
                    "name": "Криминал",
                    "slug": "kriminal",
                    "language": "rus",
                    "games_count": 654,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42623,
                    "name": "Кинематографичная",
                    "slug": "kinematografichnaia",
                    "language": "rus",
                    "games_count": 1213,
                    "image_background": "https://media.rawg.io/media/games/490/49016e06ae2103881ff6373248843069.jpg"
                },
                {
                    "id": 142,
                    "name": "Detective",
                    "slug": "detective",
                    "language": "eng",
                    "games_count": 2698,
                    "image_background": "https://media.rawg.io/media/games/cee/cee577e2097a59b77193fe2bce94667d.jpg"
                },
                {
                    "id": 42526,
                    "name": "Детектив",
                    "slug": "detektiv",
                    "language": "rus",
                    "games_count": 1188,
                    "image_background": "https://media.rawg.io/media/games/e2d/e2d3f396b16dded0f841c17c9799a882.jpg"
                },
                {
                    "id": 209,
                    "name": "Drama",
                    "slug": "drama",
                    "language": "eng",
                    "games_count": 2653,
                    "image_background": "https://media.rawg.io/media/games/b0a/b0a370527fea0e824225269d4a8797db.jpg"
                },
                {
                    "id": 42650,
                    "name": "Драма",
                    "slug": "drama-2",
                    "language": "rus",
                    "games_count": 2018,
                    "image_background": "https://media.rawg.io/media/games/883/883bc3050f9a4115d1968ece56bddfc2.jpg"
                },
                {
                    "id": 291,
                    "name": "Conspiracy",
                    "slug": "conspiracy",
                    "language": "eng",
                    "games_count": 591,
                    "image_background": "https://media.rawg.io/media/screenshots/3bc/3bc5be3c955655e4ae46dee83f5217e5.jpg"
                },
                {
                    "id": 42641,
                    "name": "Заговор",
                    "slug": "zagovor",
                    "language": "rus",
                    "games_count": 360,
                    "image_background": "https://media.rawg.io/media/games/123/123e035701a975f5d96c233f4048eed2.jpg"
                },
                {
                    "id": 326,
                    "name": "Investigation",
                    "slug": "investigation",
                    "language": "eng",
                    "games_count": 1641,
                    "image_background": "https://media.rawg.io/media/games/702/7020d1319d09e0c6a840aa08c5ce120f.jpg"
                },
                {
                    "id": 42632,
                    "name": "Боевые искусства",
                    "slug": "boevye-iskusstva",
                    "language": "rus",
                    "games_count": 338,
                    "image_background": "https://media.rawg.io/media/games/684/684ecc08397479de72c5f89ef6f16f4f.jpg"
                },
                {
                    "id": 42700,
                    "name": "Логика",
                    "slug": "logika",
                    "language": "rus",
                    "games_count": 2446,
                    "image_background": "https://media.rawg.io/media/screenshots/066/066eb1b7a3f332b8089645fbf8c3ebdc.jpg"
                },
                {
                    "id": 240,
                    "name": "Martial Arts",
                    "slug": "martial-arts",
                    "language": "eng",
                    "games_count": 323,
                    "image_background": "https://media.rawg.io/media/games/257/257c497aa4060f4a697ccbf5e99ec230.jpg"
                },
                {
                    "id": 575,
                    "name": "Logic",
                    "slug": "logic",
                    "language": "eng",
                    "games_count": 3215,
                    "image_background": "https://media.rawg.io/media/games/186/1864ee956f171b4c3d5791b82c15df2f.jpg"
                },
                {
                    "id": 42604,
                    "name": "Азартная",
                    "slug": "azartnaia",
                    "language": "rus",
                    "games_count": 156,
                    "image_background": "https://media.rawg.io/media/games/b1c/b1cd7434177e0f47ef1e4597f5701f13.jpg"
                },
                {
                    "id": 294,
                    "name": "Gambling",
                    "slug": "gambling",
                    "language": "eng",
                    "games_count": 334,
                    "image_background": "https://media.rawg.io/media/screenshots/5b6/5b6314d9b0dd5a99123820cb331484e5.jpg"
                },
                {
                    "id": 325,
                    "name": "Foreign",
                    "slug": "foreign",
                    "language": "eng",
                    "games_count": 207,
                    "image_background": "https://media.rawg.io/media/games/b6b/b6b20bfc4b34e312dbc8aac53c95a348.jpg"
                },
                {
                    "id": 66534,
                    "name": "Расследования",
                    "slug": "rassledovaniia",
                    "language": "rus",
                    "games_count": 736,
                    "image_background": "https://media.rawg.io/media/games/b23/b23e516c7c846435b9e7708a73207b67.jpg"
                },
                {
                    "id": 75152,
                    "name": "Зарубежная",
                    "slug": "zarubezhnaia",
                    "language": "rus",
                    "games_count": 78,
                    "image_background": "https://media.rawg.io/media/screenshots/520/520cfeafd3977f411b1ea069fcffd2e5.jpg"
                },
                {
                    "id": 49961,
                    "name": "3D Fighter",
                    "slug": "3d-fighter-2",
                    "language": "eng",
                    "games_count": 584,
                    "image_background": "https://media.rawg.io/media/games/e69/e69fae35b4e3afe8f6357c01fa6a0e6c.jpg"
                },
                {
                    "id": 56826,
                    "name": "3D-файтинг",
                    "slug": "3d-faiting",
                    "language": "eng",
                    "games_count": 538,
                    "image_background": "https://media.rawg.io/media/screenshots/f5f/f5fb00799bee2ab28c4a7c0a93d567b7.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 62,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/338/33848ebb15683ea022c08f39f01b810f.jpg"
                },
                {
                    "id": 3016842,
                    "image": "https://media.rawg.io/media/screenshots/134/1345e4befdd0bd8ce440db9b92f2d424.jpg"
                },
                {
                    "id": 3016843,
                    "image": "https://media.rawg.io/media/screenshots/265/265a987743a92712b19804dd06b32521.jpg"
                },
                {
                    "id": 3016844,
                    "image": "https://media.rawg.io/media/screenshots/921/921155602c0f0d601c4ab0736ce3ad77.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "fire-emblem-warriors-three-hopes",
            "name": "Fire Emblem Warriors: Three Hopes",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2022-06-24",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/073/073b560fa5ab283c03e4a9a698d001af.jpg",
            "rating": 4.43,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 5,
                    "percent": 71.43
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 2,
                    "percent": 28.57
                }
            ],
            "ratings_count": 7,
            "reviews_text_count": 0,
            "added": 56,
            "added_by_status": {
                "yet": 8,
                "owned": 9,
                "beaten": 8,
                "toplay": 22,
                "dropped": 4,
                "playing": 5
            },
            "metacritic": 80,
            "suggestions_count": 329,
            "updated": "2023-02-06T14:43:21",
            "id": 736265,
            "score": None,
            "clip": None,
            "tags": [],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 7,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/073/073b560fa5ab283c03e4a9a698d001af.jpg"
                },
                {
                    "id": 3230828,
                    "image": "https://media.rawg.io/media/screenshots/8f5/8f596c58c4377a38ff2258d90377b79e.jpg"
                },
                {
                    "id": 3230829,
                    "image": "https://media.rawg.io/media/screenshots/3d1/3d1d65fe00989cfc85acdbdd62128f4b.jpg"
                },
                {
                    "id": 3230830,
                    "image": "https://media.rawg.io/media/screenshots/0aa/0aad525c2290c9a092cdbd63272bdb05.jpg"
                },
                {
                    "id": 3230831,
                    "image": "https://media.rawg.io/media/screenshots/d4c/d4c30d5e701ac3688528a53085e4c058.jpg"
                },
                {
                    "id": 3230832,
                    "image": "https://media.rawg.io/media/screenshots/93b/93b0108e7a6b096980830cf01b4b2b0b.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "lost-judgment",
            "name": "Lost Judgment",
            "playtime": 6,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2021-09-24",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/186/1864ee956f171b4c3d5791b82c15df2f.jpg",
            "rating": 4.42,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 28,
                    "percent": 65.12
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 9,
                    "percent": 20.93
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 4,
                    "percent": 9.3
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 2,
                    "percent": 4.65
                }
            ],
            "ratings_count": 39,
            "reviews_text_count": 4,
            "added": 481,
            "added_by_status": {
                "yet": 45,
                "owned": 262,
                "beaten": 30,
                "toplay": 133,
                "dropped": 4,
                "playing": 7
            },
            "metacritic": 82,
            "suggestions_count": 418,
            "updated": "2023-04-16T07:26:11",
            "id": 600924,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42477,
                    "name": "Мрачная",
                    "slug": "mrachnaia",
                    "language": "rus",
                    "games_count": 3416,
                    "image_background": "https://media.rawg.io/media/games/d9f/d9f982e042df6263684ba1fdea3efc1c.jpg"
                },
                {
                    "id": 41,
                    "name": "Dark",
                    "slug": "dark",
                    "language": "eng",
                    "games_count": 14620,
                    "image_background": "https://media.rawg.io/media/games/ffe/ffed87105b14f5beff72ff44a7793fd5.jpg"
                },
                {
                    "id": 42487,
                    "name": "Слэшер",
                    "slug": "slesher",
                    "language": "rus",
                    "games_count": 1862,
                    "image_background": "https://media.rawg.io/media/games/21a/21ad672cedee9b4378abb6c2d2e626ee.jpg"
                },
                {
                    "id": 68,
                    "name": "Hack and Slash",
                    "slug": "hack-and-slash",
                    "language": "eng",
                    "games_count": 3414,
                    "image_background": "https://media.rawg.io/media/games/af7/af7a831001c5c32c46e950cc883b8cb7.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5545,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 42460,
                    "name": "Реализм",
                    "slug": "realizm",
                    "language": "rus",
                    "games_count": 3621,
                    "image_background": "https://media.rawg.io/media/games/bff/bff7d82316cddea9541261a045ba008a.jpg"
                },
                {
                    "id": 110,
                    "name": "Cinematic",
                    "slug": "cinematic",
                    "language": "eng",
                    "games_count": 1313,
                    "image_background": "https://media.rawg.io/media/games/7ac/7aca7ccf0e70cd0974cb899ab9e5158e.jpg"
                },
                {
                    "id": 77,
                    "name": "Realistic",
                    "slug": "realistic",
                    "language": "eng",
                    "games_count": 3658,
                    "image_background": "https://media.rawg.io/media/games/106/1069e754e7e6012b0cf42b4b04704792.jpg"
                },
                {
                    "id": 203,
                    "name": "Beat 'em up",
                    "slug": "beat-em-up",
                    "language": "eng",
                    "games_count": 2747,
                    "image_background": "https://media.rawg.io/media/games/c40/c40f9f0a3d1b4601a7a44d230c95f126.jpg"
                },
                {
                    "id": 144,
                    "name": "Crime",
                    "slug": "crime",
                    "language": "eng",
                    "games_count": 2580,
                    "image_background": "https://media.rawg.io/media/games/9e5/9e5b274c7e3aa5e30beba31b834b0e7e.jpg"
                },
                {
                    "id": 42443,
                    "name": "Криминал",
                    "slug": "kriminal",
                    "language": "rus",
                    "games_count": 657,
                    "image_background": "https://media.rawg.io/media/games/e2d/e2d3f396b16dded0f841c17c9799a882.jpg"
                },
                {
                    "id": 42623,
                    "name": "Кинематографичная",
                    "slug": "kinematografichnaia",
                    "language": "rus",
                    "games_count": 1219,
                    "image_background": "https://media.rawg.io/media/games/708/7080e6c87e0825cb02888bf3c44b3889.jpg"
                },
                {
                    "id": 142,
                    "name": "Detective",
                    "slug": "detective",
                    "language": "eng",
                    "games_count": 2708,
                    "image_background": "https://media.rawg.io/media/games/3ca/3ca24180cb8d9780d45f394f685fd9d2.jpg"
                },
                {
                    "id": 42526,
                    "name": "Детектив",
                    "slug": "detektiv",
                    "language": "rus",
                    "games_count": 1193,
                    "image_background": "https://media.rawg.io/media/screenshots/53b/53b07d7d8979bd4a5cb4e484c7aacc33.jpg"
                },
                {
                    "id": 209,
                    "name": "Drama",
                    "slug": "drama",
                    "language": "eng",
                    "games_count": 2671,
                    "image_background": "https://media.rawg.io/media/games/b0a/b0a370527fea0e824225269d4a8797db.jpg"
                },
                {
                    "id": 42650,
                    "name": "Драма",
                    "slug": "drama-2",
                    "language": "rus",
                    "games_count": 2034,
                    "image_background": "https://media.rawg.io/media/games/f0a/f0a65d7d9c4534f8f4897f9d161307ed.jpg"
                },
                {
                    "id": 291,
                    "name": "Conspiracy",
                    "slug": "conspiracy",
                    "language": "eng",
                    "games_count": 594,
                    "image_background": "https://media.rawg.io/media/games/c14/c14d85f2ec10e82e3d5cd837c9c0a56d.jpg"
                },
                {
                    "id": 42641,
                    "name": "Заговор",
                    "slug": "zagovor",
                    "language": "rus",
                    "games_count": 362,
                    "image_background": "https://media.rawg.io/media/games/f1d/f1d25c007b9b45c98b57ff9ebbca9692.jpg"
                },
                {
                    "id": 326,
                    "name": "Investigation",
                    "slug": "investigation",
                    "language": "eng",
                    "games_count": 1649,
                    "image_background": "https://media.rawg.io/media/games/dbb/dbba6100aae179b5f24052c9141d426d.jpg"
                },
                {
                    "id": 151,
                    "name": "Modern",
                    "slug": "modern",
                    "language": "eng",
                    "games_count": 1056,
                    "image_background": "https://media.rawg.io/media/games/8b9/8b9e77be7f0f7941b11ae4b21ca2db43.jpg"
                },
                {
                    "id": 42528,
                    "name": "Современность",
                    "slug": "sovremennost",
                    "language": "rus",
                    "games_count": 851,
                    "image_background": "https://media.rawg.io/media/screenshots/ae0/ae0bb3c16d0660acb18b197d5856baf8.jpg"
                },
                {
                    "id": 42700,
                    "name": "Логика",
                    "slug": "logika",
                    "language": "rus",
                    "games_count": 2461,
                    "image_background": "https://media.rawg.io/media/games/186/1864ee956f171b4c3d5791b82c15df2f.jpg"
                },
                {
                    "id": 42632,
                    "name": "Боевые искусства",
                    "slug": "boevye-iskusstva",
                    "language": "rus",
                    "games_count": 340,
                    "image_background": "https://media.rawg.io/media/screenshots/b5d/b5d8f5ac511033013e57ec96472c20d6.jpg"
                },
                {
                    "id": 240,
                    "name": "Martial Arts",
                    "slug": "martial-arts",
                    "language": "eng",
                    "games_count": 325,
                    "image_background": "https://media.rawg.io/media/screenshots/b5d/b5d8f5ac511033013e57ec96472c20d6.jpg"
                },
                {
                    "id": 575,
                    "name": "Logic",
                    "slug": "logic",
                    "language": "eng",
                    "games_count": 3232,
                    "image_background": "https://media.rawg.io/media/screenshots/636/6362ea628efa7a79b20eb647cb14555c.jpg"
                },
                {
                    "id": 42604,
                    "name": "Азартная",
                    "slug": "azartnaia",
                    "language": "rus",
                    "games_count": 160,
                    "image_background": "https://media.rawg.io/media/screenshots/74d/74d451659590ee4100d9e9f850e11974.jpg"
                },
                {
                    "id": 294,
                    "name": "Gambling",
                    "slug": "gambling",
                    "language": "eng",
                    "games_count": 338,
                    "image_background": "https://media.rawg.io/media/games/a1c/a1cf8e234ea9dc6218682e3eab56e418.jpg"
                },
                {
                    "id": 325,
                    "name": "Foreign",
                    "slug": "foreign",
                    "language": "eng",
                    "games_count": 213,
                    "image_background": "https://media.rawg.io/media/screenshots/f4a/f4a5b19f713695c5ee6bb01be63b6b5b.jpg"
                },
                {
                    "id": 66534,
                    "name": "Расследования",
                    "slug": "rassledovaniia",
                    "language": "rus",
                    "games_count": 743,
                    "image_background": "https://media.rawg.io/media/games/add/add2aecd96e74df7e27082328039957e.jpg"
                },
                {
                    "id": 75152,
                    "name": "Зарубежная",
                    "slug": "zarubezhnaia",
                    "language": "rus",
                    "games_count": 84,
                    "image_background": "https://media.rawg.io/media/screenshots/f4a/f4a5b19f713695c5ee6bb01be63b6b5b.jpg"
                },
                {
                    "id": 49961,
                    "name": "3D Fighter",
                    "slug": "3d-fighter-2",
                    "language": "eng",
                    "games_count": 590,
                    "image_background": "https://media.rawg.io/media/screenshots/f5f/f5fb00799bee2ab28c4a7c0a93d567b7.jpg"
                },
                {
                    "id": 56826,
                    "name": "3D-файтинг",
                    "slug": "3d-faiting",
                    "language": "eng",
                    "games_count": 544,
                    "image_background": "https://media.rawg.io/media/screenshots/3b4/3b497b95af2054897ddfee0ccc1afd7f_PyAIfVh.jpg"
                }
            ],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 43,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/186/1864ee956f171b4c3d5791b82c15df2f.jpg"
                },
                {
                    "id": 2836337,
                    "image": "https://media.rawg.io/media/screenshots/e59/e598e4c50abdf231b9c59f324db710f0.jpg"
                },
                {
                    "id": 2836338,
                    "image": "https://media.rawg.io/media/screenshots/1e0/1e05031ae168e4d4dd3214d97bfc2765.jpg"
                },
                {
                    "id": 2836339,
                    "image": "https://media.rawg.io/media/screenshots/425/425f9596e064b899c320261cc3399f7a.jpg"
                },
                {
                    "id": 2836340,
                    "image": "https://media.rawg.io/media/screenshots/809/809e0eb286f2effb81e9a35388f556a0.jpg"
                },
                {
                    "id": 2836341,
                    "image": "https://media.rawg.io/media/screenshots/7a1/7a1cb29cb6e51d323c0e1625fe42e41d.jpg"
                },
                {
                    "id": 2836342,
                    "image": "https://media.rawg.io/media/screenshots/8f4/8f449b338c10a8a5c3a4793dfc744091.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "the-last-of-us-part-2",
            "name": "The Last of Us Part II",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2020-06-19",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/909/909974d1c7863c2027241e265fe7011f.jpg",
            "rating": 4.42,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 1178,
                    "percent": 70.33
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 262,
                    "percent": 15.64
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 123,
                    "percent": 7.34
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 112,
                    "percent": 6.69
                }
            ],
            "ratings_count": 1599,
            "reviews_text_count": 57,
            "added": 6399,
            "added_by_status": {
                "yet": 337,
                "owned": 3010,
                "beaten": 1537,
                "toplay": 1319,
                "dropped": 67,
                "playing": 129
            },
            "metacritic": 93,
            "suggestions_count": 584,
            "updated": "2023-04-16T07:21:11",
            "id": 51325,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 1,
                    "name": "Survival",
                    "slug": "survival",
                    "language": "eng",
                    "games_count": 7130,
                    "image_background": "https://media.rawg.io/media/games/d7d/d7d33daa1892e2468cd0263d5dfc957e.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 15,
                    "name": "Stealth",
                    "slug": "stealth",
                    "language": "eng",
                    "games_count": 5846,
                    "image_background": "https://media.rawg.io/media/games/16b/16b1b7b36e2042d1128d5a3e852b3b2f.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 86,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 270,
                    "name": "Blood",
                    "slug": "blood",
                    "language": "eng",
                    "games_count": 1984,
                    "image_background": "https://media.rawg.io/media/games/63f/63f0e68688cad279ed38cde931dbfcdb.jpg"
                },
                {
                    "id": 78,
                    "name": "America",
                    "slug": "america",
                    "language": "eng",
                    "games_count": 440,
                    "image_background": "https://media.rawg.io/media/games/4c2/4c23c4a88f53e7e482d72ddfcf5b9b41.jpg"
                },
                {
                    "id": 42410,
                    "name": "LGBTQ+",
                    "slug": "lgbtq-2",
                    "language": "eng",
                    "games_count": 1140,
                    "image_background": "https://media.rawg.io/media/screenshots/f37/f37a6ef6d58c92b21410861734d61c69.jpeg"
                },
                {
                    "id": 467,
                    "name": "Role Playing Game",
                    "slug": "role-playing-game",
                    "language": "eng",
                    "games_count": 18,
                    "image_background": "https://media.rawg.io/media/games/bac/bac558c863989fadc4fede908c15cd64.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 1675,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/909/909974d1c7863c2027241e265fe7011f.jpg"
                },
                {
                    "id": 802461,
                    "image": "https://media.rawg.io/media/screenshots/5a8/5a8f06949b0264aa27374d3f005a2842.jpg"
                },
                {
                    "id": 802463,
                    "image": "https://media.rawg.io/media/screenshots/160/1603055e1fc4fbbea395809242d23c67_CDpXDx3.jpg"
                },
                {
                    "id": 802464,
                    "image": "https://media.rawg.io/media/screenshots/e9c/e9cfbbc7821827e04c890ecf087c246c.jpg"
                },
                {
                    "id": 802466,
                    "image": "https://media.rawg.io/media/screenshots/e58/e58f17219570ca451356f6eec746e697.jpg"
                },
                {
                    "id": 802467,
                    "image": "https://media.rawg.io/media/screenshots/02a/02aede3e5e6738e37ff1240c1c2fcee8.jpg"
                },
                {
                    "id": 802468,
                    "image": "https://media.rawg.io/media/screenshots/5ea/5ea913f25ebb5454571e8d92deddebcc.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 2,
                    "name": "Shooter",
                    "slug": "shooter"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "katana-zero",
            "name": "Katana ZERO",
            "playtime": 5,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "macOS",
                        "slug": "macos"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 5,
                        "name": "GOG",
                        "slug": "gog"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2019-04-17",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/d37/d37e110ddcc0bd52d99f0f647b737a0a.jpg",
            "rating": 4.42,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 530,
                    "percent": 55.85
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 331,
                    "percent": 34.88
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 64,
                    "percent": 6.74
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 24,
                    "percent": 2.53
                }
            ],
            "ratings_count": 933,
            "reviews_text_count": 10,
            "added": 3572,
            "added_by_status": {
                "yet": 195,
                "owned": 1861,
                "beaten": 909,
                "toplay": 411,
                "dropped": 131,
                "playing": 65
            },
            "metacritic": 83,
            "suggestions_count": 287,
            "updated": "2023-04-16T07:32:29",
            "id": 13856,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 45,
                    "name": "2D",
                    "slug": "2d",
                    "language": "eng",
                    "games_count": 200870,
                    "image_background": "https://media.rawg.io/media/games/f46/f466571d536f2e3ea9e815ad17177501.jpg"
                },
                {
                    "id": 42423,
                    "name": "Научная фантастика",
                    "slug": "nauchnaia-fantastika",
                    "language": "rus",
                    "games_count": 5796,
                    "image_background": "https://media.rawg.io/media/games/3cf/3cff89996570cf29a10eb9cd967dcf73.jpg"
                },
                {
                    "id": 42420,
                    "name": "Сложная",
                    "slug": "slozhnaia",
                    "language": "rus",
                    "games_count": 4385,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 42491,
                    "name": "Мясо",
                    "slug": "miaso",
                    "language": "rus",
                    "games_count": 3850,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 42463,
                    "name": "Платформер",
                    "slug": "platformer-2",
                    "language": "rus",
                    "games_count": 6297,
                    "image_background": "https://media.rawg.io/media/games/89a/89a700d3c6a76bd0610ca89ccd20da54.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 42415,
                    "name": "Пиксельная графика",
                    "slug": "pikselnaia-grafika",
                    "language": "rus",
                    "games_count": 8585,
                    "image_background": "https://media.rawg.io/media/games/bbf/bbf8d74ab64440ad76294cff2f4d9cfa.jpg"
                },
                {
                    "id": 42467,
                    "name": "Ретро",
                    "slug": "retro-2",
                    "language": "rus",
                    "games_count": 5520,
                    "image_background": "https://media.rawg.io/media/games/9fa/9fa63622543e5d4f6d99aa9d73b043de.jpg"
                },
                {
                    "id": 122,
                    "name": "Pixel Graphics",
                    "slug": "pixel-graphics",
                    "language": "eng",
                    "games_count": 95727,
                    "image_background": "https://media.rawg.io/media/screenshots/d68/d684c5ec81b8ea46bfd4b5c3bae4007f.jpg"
                },
                {
                    "id": 74,
                    "name": "Retro",
                    "slug": "retro",
                    "language": "eng",
                    "games_count": 41775,
                    "image_background": "https://media.rawg.io/media/screenshots/6fe/6fe228662a253cd929cc78a103541ee0.jpg"
                },
                {
                    "id": 42487,
                    "name": "Слэшер",
                    "slug": "slesher",
                    "language": "rus",
                    "games_count": 1862,
                    "image_background": "https://media.rawg.io/media/games/21a/21ad672cedee9b4378abb6c2d2e626ee.jpg"
                },
                {
                    "id": 42612,
                    "name": "Быстрая",
                    "slug": "bystraia",
                    "language": "rus",
                    "games_count": 1499,
                    "image_background": "https://media.rawg.io/media/games/a01/a01b34c722ceec784817381eb1824fa5.jpg"
                },
                {
                    "id": 42470,
                    "name": "Киберпанк",
                    "slug": "kiberpank",
                    "language": "rus",
                    "games_count": 1301,
                    "image_background": "https://media.rawg.io/media/games/b72/b7233d5d5b1e75e86bb860ccc7aeca85.jpg"
                },
                {
                    "id": 226,
                    "name": "Cyberpunk",
                    "slug": "cyberpunk",
                    "language": "eng",
                    "games_count": 4177,
                    "image_background": "https://media.rawg.io/media/games/2e1/2e187b31e5cee21c110bd16798d75fab.jpg"
                },
                {
                    "id": 1465,
                    "name": "combat",
                    "slug": "combat",
                    "language": "eng",
                    "games_count": 9132,
                    "image_background": "https://media.rawg.io/media/games/0a5/0a56e2bb9ce95359e69ff9689c553a45.jpg"
                },
                {
                    "id": 406,
                    "name": "Story",
                    "slug": "story",
                    "language": "eng",
                    "games_count": 11617,
                    "image_background": "https://media.rawg.io/media/games/2ee/2eeed8524931b4fae1e4a40d0e5443b5.jpg"
                },
                {
                    "id": 42462,
                    "name": "Метроидвания",
                    "slug": "metroidvaniia",
                    "language": "rus",
                    "games_count": 899,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42584,
                    "name": "Ниндзя",
                    "slug": "nindzia",
                    "language": "rus",
                    "games_count": 362,
                    "image_background": "https://media.rawg.io/media/screenshots/157/1571cdfb52888191eabaf53c2b897240.jpg"
                },
                {
                    "id": 42622,
                    "name": "Нуар",
                    "slug": "nuar",
                    "language": "rus",
                    "games_count": 495,
                    "image_background": "https://media.rawg.io/media/games/c68/c689b61ea646f219c4609073eb41626f.jpg"
                },
                {
                    "id": 42570,
                    "name": "Контроль времени",
                    "slug": "kontrol-vremeni",
                    "language": "rus",
                    "games_count": 403,
                    "image_background": "https://media.rawg.io/media/games/702/7020d1319d09e0c6a840aa08c5ce120f.jpg"
                },
                {
                    "id": 974,
                    "name": "death",
                    "slug": "death",
                    "language": "eng",
                    "games_count": 3867,
                    "image_background": "https://media.rawg.io/media/games/f61/f61cc8e0bce08615d90918e428aa5dc9.jpg"
                },
                {
                    "id": 704,
                    "name": "Traps",
                    "slug": "traps",
                    "language": "eng",
                    "games_count": 2248,
                    "image_background": "https://media.rawg.io/media/screenshots/304/304a2745890843f7ba55acfd836663b5.jpg"
                },
                {
                    "id": 2489,
                    "name": "dodge",
                    "slug": "dodge",
                    "language": "eng",
                    "games_count": 3092,
                    "image_background": "https://media.rawg.io/media/screenshots/443/443c175b136c352d51dd0a7c080de65e.jpg"
                },
                {
                    "id": 2743,
                    "name": "dash",
                    "slug": "dash",
                    "language": "eng",
                    "games_count": 2390,
                    "image_background": "https://media.rawg.io/media/screenshots/9a0/9a016183ff8e620fcc4bd06f9a781ba5.jpg"
                }
            ],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 949,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/d37/d37e110ddcc0bd52d99f0f647b737a0a.jpg"
                },
                {
                    "id": 119448,
                    "image": "https://media.rawg.io/media/screenshots/d4e/d4e033c1b504f7df5fb234287e28e990.jpg"
                },
                {
                    "id": 119449,
                    "image": "https://media.rawg.io/media/screenshots/bc9/bc9fd02f32749fe15581bf8b692d7814.jpg"
                },
                {
                    "id": 119450,
                    "image": "https://media.rawg.io/media/screenshots/3cc/3cc5aec6ba38ff277ac0d0be4573ec62.jpg"
                },
                {
                    "id": 119451,
                    "image": "https://media.rawg.io/media/screenshots/5d1/5d154940b0b5fb5d3e99ff3c6d4f9b9e.jpg"
                },
                {
                    "id": 119452,
                    "image": "https://media.rawg.io/media/screenshots/18b/18b9df6ba9fac61589376c96735e5a02.jpg"
                },
                {
                    "id": 119453,
                    "image": "https://media.rawg.io/media/screenshots/f48/f48df10956744670bbd6cf7f14c5b511.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "Apple Macintosh",
                        "slug": "mac"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "judgment-2",
            "name": "Judgment (2019)",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2019-06-25",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/cf9/cf9ab5aee88c6db2cc5cf31d30aef5b8.jpg",
            "rating": 4.41,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 47,
                    "percent": 69.12
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 12,
                    "percent": 17.65
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 5,
                    "percent": 7.35
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 4,
                    "percent": 5.88
                }
            ],
            "ratings_count": 63,
            "reviews_text_count": 4,
            "added": 576,
            "added_by_status": {
                "yet": 46,
                "owned": 266,
                "beaten": 58,
                "toplay": 177,
                "dropped": 12,
                "playing": 17
            },
            "metacritic": 82,
            "suggestions_count": 502,
            "updated": "2021-06-29T12:43:35",
            "id": 248397,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 41,
                    "name": "Dark",
                    "slug": "dark",
                    "language": "eng",
                    "games_count": 7537,
                    "image_background": "https://media.rawg.io/media/games/d9f/d9f982e042df6263684ba1fdea3efc1c.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4514,
                    "image_background": "https://media.rawg.io/media/games/2a2/2a2f9a0035544500e59a171c7038ec3a.jpg"
                },
                {
                    "id": 117,
                    "name": "Mystery",
                    "slug": "mystery",
                    "language": "eng",
                    "games_count": 7196,
                    "image_background": "https://media.rawg.io/media/games/bc6/bc6b163403504d0c041253749e233ed3.jpg"
                },
                {
                    "id": 37797,
                    "name": "true exclusive",
                    "slug": "true-exclusive",
                    "language": "eng",
                    "games_count": 3996,
                    "image_background": "https://media.rawg.io/media/games/dfa/dfa0906773ebb8a50d15548ac5b8ee5e.jpg"
                },
                {
                    "id": 144,
                    "name": "Crime",
                    "slug": "crime",
                    "language": "eng",
                    "games_count": 1840,
                    "image_background": "https://media.rawg.io/media/games/a34/a348e613424260bc7e034fb6031c762e.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 82,
                    "image_background": "https://media.rawg.io/media/games/909/909974d1c7863c2027241e265fe7011f.jpg"
                },
                {
                    "id": 1465,
                    "name": "combat",
                    "slug": "combat",
                    "language": "eng",
                    "games_count": 5085,
                    "image_background": "https://media.rawg.io/media/games/848/8482235332f4518da363c3cb4e5cd075.jpg"
                },
                {
                    "id": 981,
                    "name": "battle",
                    "slug": "battle",
                    "language": "eng",
                    "games_count": 8978,
                    "image_background": "https://media.rawg.io/media/games/fd6/fd6a1eecd3ec0f875f1924f3656b7dd9.jpg"
                },
                {
                    "id": 183,
                    "name": "Thriller",
                    "slug": "thriller",
                    "language": "eng",
                    "games_count": 942,
                    "image_background": "https://media.rawg.io/media/games/066/066440c8ba08c0a28931797a0084798a.jpg"
                },
                {
                    "id": 2889,
                    "name": "balance",
                    "slug": "balance",
                    "language": "eng",
                    "games_count": 1367,
                    "image_background": "https://media.rawg.io/media/games/c51/c511b48dbaa5e1ca5f02a94b5cc70b31.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 68,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/cf9/cf9ab5aee88c6db2cc5cf31d30aef5b8.jpg"
                },
                {
                    "id": 2810356,
                    "image": "https://media.rawg.io/media/screenshots/49a/49a202fc4f2c10b54527de5e3e1495d8.jpg"
                },
                {
                    "id": 2810357,
                    "image": "https://media.rawg.io/media/screenshots/487/4874a2d2929d4d0df5b4cd03f086b3ca.jpg"
                },
                {
                    "id": 2810358,
                    "image": "https://media.rawg.io/media/screenshots/05b/05b222888c99ec0965686f9ef6763b76.jpg"
                },
                {
                    "id": 2810359,
                    "image": "https://media.rawg.io/media/screenshots/ded/ded4c958f071507d554e042c24e78819.jpg"
                },
                {
                    "id": 2810360,
                    "image": "https://media.rawg.io/media/screenshots/e74/e740036beae953c771f78a5bfad85596.jpg"
                },
                {
                    "id": 2810361,
                    "image": "https://media.rawg.io/media/screenshots/b26/b26239ffab93a1883d07141c69b80f30.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "huntdown",
            "name": "HUNTDOWN",
            "playtime": 2,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "iOS",
                        "slug": "ios"
                    }
                },
                {
                    "platform": {
                        "id": 21,
                        "name": "Android",
                        "slug": "android"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "macOS",
                        "slug": "macos"
                    }
                },
                {
                    "platform": {
                        "id": 6,
                        "name": "Linux",
                        "slug": "linux"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 4,
                        "name": "App Store",
                        "slug": "apple-appstore"
                    }
                },
                {
                    "store": {
                        "id": 5,
                        "name": "GOG",
                        "slug": "gog"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                },
                {
                    "store": {
                        "id": 11,
                        "name": "Epic Games",
                        "slug": "epic-games"
                    }
                }
            ],
            "released": "2020-05-12",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/5cb/5cb897cd1000906d2467ea4d0bdf1af4.jpg",
            "rating": 4.41,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 38,
                    "percent": 60.32
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 17,
                    "percent": 26.98
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 6,
                    "percent": 9.52
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 2,
                    "percent": 3.17
                }
            ],
            "ratings_count": 58,
            "reviews_text_count": 3,
            "added": 481,
            "added_by_status": {
                "yet": 22,
                "owned": 347,
                "beaten": 30,
                "toplay": 59,
                "dropped": 16,
                "playing": 7
            },
            "metacritic": 85,
            "suggestions_count": 359,
            "updated": "2022-12-22T00:37:40",
            "id": 28159,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 18,
                    "name": "Co-op",
                    "slug": "co-op",
                    "language": "eng",
                    "games_count": 9806,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 42428,
                    "name": "Шутер",
                    "slug": "shuter",
                    "language": "rus",
                    "games_count": 6479,
                    "image_background": "https://media.rawg.io/media/games/c24/c24ec439abf4a2e92f3429dfa83f7f94.jpg"
                },
                {
                    "id": 45,
                    "name": "2D",
                    "slug": "2d",
                    "language": "eng",
                    "games_count": 200870,
                    "image_background": "https://media.rawg.io/media/games/f46/f466571d536f2e3ea9e815ad17177501.jpg"
                },
                {
                    "id": 198,
                    "name": "Split Screen",
                    "slug": "split-screen",
                    "language": "eng",
                    "games_count": 5537,
                    "image_background": "https://media.rawg.io/media/games/27b/27b02ffaab6b250cc31bf43baca1fc34.jpg"
                },
                {
                    "id": 75,
                    "name": "Local Co-Op",
                    "slug": "local-co-op",
                    "language": "eng",
                    "games_count": 5032,
                    "image_background": "https://media.rawg.io/media/games/926/926928beb8a9f9b31cf202965aa4cbbc.jpg"
                },
                {
                    "id": 42415,
                    "name": "Пиксельная графика",
                    "slug": "pikselnaia-grafika",
                    "language": "rus",
                    "games_count": 8585,
                    "image_background": "https://media.rawg.io/media/games/bbf/bbf8d74ab64440ad76294cff2f4d9cfa.jpg"
                },
                {
                    "id": 42467,
                    "name": "Ретро",
                    "slug": "retro-2",
                    "language": "rus",
                    "games_count": 5520,
                    "image_background": "https://media.rawg.io/media/games/9fa/9fa63622543e5d4f6d99aa9d73b043de.jpg"
                },
                {
                    "id": 72,
                    "name": "Local Multiplayer",
                    "slug": "local-multiplayer",
                    "language": "eng",
                    "games_count": 12874,
                    "image_background": "https://media.rawg.io/media/games/aa3/aa36ba4b486a03ddfaef274fb4f5afd4.jpg"
                },
                {
                    "id": 42469,
                    "name": "Вид сбоку",
                    "slug": "vid-sboku",
                    "language": "rus",
                    "games_count": 2911,
                    "image_background": "https://media.rawg.io/media/games/a5a/a5abaa1b5cc1567b026fa3aa9fbd828e.jpg"
                },
                {
                    "id": 42470,
                    "name": "Киберпанк",
                    "slug": "kiberpank",
                    "language": "rus",
                    "games_count": 1301,
                    "image_background": "https://media.rawg.io/media/games/b72/b7233d5d5b1e75e86bb860ccc7aeca85.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 63,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/5cb/5cb897cd1000906d2467ea4d0bdf1af4.jpg"
                },
                {
                    "id": 269439,
                    "image": "https://media.rawg.io/media/screenshots/015/015a741d966b316ce465613805519602.jpg"
                },
                {
                    "id": 269440,
                    "image": "https://media.rawg.io/media/screenshots/9dd/9dd226e9760c7164c3aa332e9e96a322.jpg"
                },
                {
                    "id": 269441,
                    "image": "https://media.rawg.io/media/screenshots/262/262e9aef0a2f20f346f189274e40747c.jpg"
                },
                {
                    "id": 269442,
                    "image": "https://media.rawg.io/media/screenshots/4b5/4b5e641136d2683cf7203c627b20d45f.jpg"
                },
                {
                    "id": 269443,
                    "image": "https://media.rawg.io/media/screenshots/6a4/6a4b4f6cc3e38f840f065f426851b2ab.jpg"
                },
                {
                    "id": 3430440,
                    "image": "https://media.rawg.io/media/screenshots/6dd/6dd6f3fd8d06e2e1fdd7d0ede15e00f5.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 4,
                        "name": "iOS",
                        "slug": "ios"
                    }
                },
                {
                    "platform": {
                        "id": 8,
                        "name": "Android",
                        "slug": "android"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "Apple Macintosh",
                        "slug": "mac"
                    }
                },
                {
                    "platform": {
                        "id": 6,
                        "name": "Linux",
                        "slug": "linux"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "metroid-dread",
            "name": "Metroid Dread",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2021-10-08",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/c26/c262f8b54b46edc72594c4a9bb8ee13e.jpg",
            "rating": 4.41,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 128,
                    "percent": 57.92
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 66,
                    "percent": 29.86
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 22,
                    "percent": 9.95
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 5,
                    "percent": 2.26
                }
            ],
            "ratings_count": 212,
            "reviews_text_count": 9,
            "added": 592,
            "added_by_status": {
                "yet": 62,
                "owned": 68,
                "beaten": 216,
                "toplay": 172,
                "dropped": 33,
                "playing": 41
            },
            "metacritic": 88,
            "suggestions_count": 438,
            "updated": "2023-04-09T13:40:35",
            "id": 622495,
            "score": None,
            "clip": None,
            "tags": [],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 221,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/c26/c262f8b54b46edc72594c4a9bb8ee13e.jpg"
                },
                {
                    "id": 2897130,
                    "image": "https://media.rawg.io/media/screenshots/0f1/0f123e7f6b6c2f5f2a3f022244356e1f.jpg"
                },
                {
                    "id": 2897131,
                    "image": "https://media.rawg.io/media/screenshots/442/442d0ab90c41a4fc2b2e21853fc64f97.jpg"
                },
                {
                    "id": 2897132,
                    "image": "https://media.rawg.io/media/screenshots/3cb/3cbf63f3ac060880f29a468fa28b7b10.jpg"
                },
                {
                    "id": 2897133,
                    "image": "https://media.rawg.io/media/screenshots/e10/e102a483c4b9aca288c9c03ed87b308b.jpg"
                },
                {
                    "id": 2897134,
                    "image": "https://media.rawg.io/media/screenshots/88a/88a8551270c4742af74a099a7ea6563c.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "hi-fi-rush",
            "name": "Hi-Fi Rush",
            "playtime": 5,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                }
            ],
            "released": "2023-01-25",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/62f/62f71917e64e913f2a893e7373319c60.jpg",
            "rating": 4.41,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 80,
                    "percent": 62.5
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 35,
                    "percent": 27.34
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 7,
                    "percent": 5.47
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 6,
                    "percent": 4.69
                }
            ],
            "ratings_count": 123,
            "reviews_text_count": 3,
            "added": 548,
            "added_by_status": {
                "yet": 49,
                "owned": 162,
                "beaten": 97,
                "toplay": 164,
                "dropped": 36,
                "playing": 40
            },
            "metacritic": 88,
            "suggestions_count": 251,
            "updated": "2023-04-16T17:36:02",
            "id": 914789,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 4,
                    "name": "Funny",
                    "slug": "funny",
                    "language": "eng",
                    "games_count": 23421,
                    "image_background": "https://media.rawg.io/media/games/c89/c89ca70716080733d03724277df2c6c7.jpg"
                },
                {
                    "id": 42463,
                    "name": "Платформер",
                    "slug": "platformer-2",
                    "language": "rus",
                    "games_count": 6297,
                    "image_background": "https://media.rawg.io/media/games/89a/89a700d3c6a76bd0610ca89ccd20da54.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 134,
                    "name": "Anime",
                    "slug": "anime",
                    "language": "eng",
                    "games_count": 11173,
                    "image_background": "https://media.rawg.io/media/games/cc5/cc576aa274780702ef93463f5410031e.jpg"
                },
                {
                    "id": 42407,
                    "name": "Аниме",
                    "slug": "anime-2",
                    "language": "rus",
                    "games_count": 6641,
                    "image_background": "https://media.rawg.io/media/games/a38/a3857b2445c70ac5dbe73b210a827ad8.jpg"
                },
                {
                    "id": 42487,
                    "name": "Слэшер",
                    "slug": "slesher",
                    "language": "rus",
                    "games_count": 1862,
                    "image_background": "https://media.rawg.io/media/games/21a/21ad672cedee9b4378abb6c2d2e626ee.jpg"
                },
                {
                    "id": 68,
                    "name": "Hack and Slash",
                    "slug": "hack-and-slash",
                    "language": "eng",
                    "games_count": 3414,
                    "image_background": "https://media.rawg.io/media/games/af7/af7a831001c5c32c46e950cc883b8cb7.jpg"
                },
                {
                    "id": 40833,
                    "name": "Captions available",
                    "slug": "captions-available",
                    "language": "eng",
                    "games_count": 1221,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 42601,
                    "name": "Цветастая",
                    "slug": "tsvetastaia",
                    "language": "rus",
                    "games_count": 8716,
                    "image_background": "https://media.rawg.io/media/games/e74/e74458058b35e01c1ae3feeb39a3f724.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5545,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 165,
                    "name": "Colorful",
                    "slug": "colorful",
                    "language": "eng",
                    "games_count": 17830,
                    "image_background": "https://media.rawg.io/media/games/c2e/c2eb6021a2596644b437e943612af25c.jpg"
                },
                {
                    "id": 42470,
                    "name": "Киберпанк",
                    "slug": "kiberpank",
                    "language": "rus",
                    "games_count": 1301,
                    "image_background": "https://media.rawg.io/media/games/b72/b7233d5d5b1e75e86bb860ccc7aeca85.jpg"
                },
                {
                    "id": 226,
                    "name": "Cyberpunk",
                    "slug": "cyberpunk",
                    "language": "eng",
                    "games_count": 4177,
                    "image_background": "https://media.rawg.io/media/games/2e1/2e187b31e5cee21c110bd16798d75fab.jpg"
                },
                {
                    "id": 136,
                    "name": "Music",
                    "slug": "music",
                    "language": "eng",
                    "games_count": 26820,
                    "image_background": "https://media.rawg.io/media/games/f99/f9979698c43fd84c3ab69280576dd3af.jpg"
                },
                {
                    "id": 42571,
                    "name": "Мультипликация",
                    "slug": "multiplikatsiia",
                    "language": "rus",
                    "games_count": 3558,
                    "image_background": "https://media.rawg.io/media/games/e44/e445335e611b4ccf03af71fffcbd30a4.jpg"
                },
                {
                    "id": 42620,
                    "name": "Музыка",
                    "slug": "muzyka",
                    "language": "rus",
                    "games_count": 945,
                    "image_background": "https://media.rawg.io/media/screenshots/695/69511e8a8ec8edf9b85c3e68190844a4.jpg"
                },
                {
                    "id": 164,
                    "name": "Cartoony",
                    "slug": "cartoony",
                    "language": "eng",
                    "games_count": 3501,
                    "image_background": "https://media.rawg.io/media/screenshots/b54/b5455f679a7e626f32ef8b78392cc327_xVnsIrO.jpg"
                },
                {
                    "id": 304,
                    "name": "Character Action Game",
                    "slug": "character-action-game",
                    "language": "eng",
                    "games_count": 537,
                    "image_background": "https://media.rawg.io/media/games/9fb/9fbf956a16249def7625ab5dc3d09515.jpg"
                },
                {
                    "id": 42495,
                    "name": "Яркий главный герой",
                    "slug": "iarkii-glavnyi-geroi",
                    "language": "rus",
                    "games_count": 553,
                    "image_background": "https://media.rawg.io/media/screenshots/33e/33e5d7f16c1d63fb50c7cf6af515df3e.jpg"
                },
                {
                    "id": 207,
                    "name": "Rhythm",
                    "slug": "rhythm",
                    "language": "eng",
                    "games_count": 1863,
                    "image_background": "https://media.rawg.io/media/screenshots/90f/90f61894908915eff8455e7b43d466a2.jpg"
                },
                {
                    "id": 42618,
                    "name": "Ритм-игра",
                    "slug": "ritm-igra",
                    "language": "rus",
                    "games_count": 725,
                    "image_background": "https://media.rawg.io/media/screenshots/ca9/ca95a5bb74f37b4a483a2e88ec604097.jpg"
                },
                {
                    "id": 42493,
                    "name": "Зрелищные сражения",
                    "slug": "zrelishchnye-srazheniia",
                    "language": "rus",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 254,
                    "name": "Spectacle fighter",
                    "slug": "spectacle-fighter",
                    "language": "eng",
                    "games_count": 386,
                    "image_background": "https://media.rawg.io/media/games/566/566f53f43aa1bd28c63cf3a4d21440ee.jpg"
                },
                {
                    "id": 12930,
                    "name": "rhytm-based",
                    "slug": "rhytm-based",
                    "language": "eng",
                    "games_count": 3,
                    "image_background": "https://media.rawg.io/media/games/e97/e974dbe25988520c63b3b2fb8b252f23.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 128,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/62f/62f71917e64e913f2a893e7373319c60.jpg"
                },
                {
                    "id": 3748611,
                    "image": "https://media.rawg.io/media/screenshots/9b0/9b046d74298d65c7f4a466a63a2e1f83.jpg"
                },
                {
                    "id": 3748612,
                    "image": "https://media.rawg.io/media/screenshots/fb5/fb54dd52f564f9c7191c18839116ca5c.jpg"
                },
                {
                    "id": 3748613,
                    "image": "https://media.rawg.io/media/screenshots/1b9/1b91fe073eeceeefce59752811c2c675.jpg"
                },
                {
                    "id": 3748614,
                    "image": "https://media.rawg.io/media/screenshots/dfb/dfb298677014b7c1b2fca160905f11b0.jpg"
                },
                {
                    "id": 3748615,
                    "image": "https://media.rawg.io/media/screenshots/b47/b47332d748e66df98dcda243d044ee48.jpg"
                },
                {
                    "id": 3748616,
                    "image": "https://media.rawg.io/media/screenshots/d53/d5397e76a7a73fd24d4b92da0477e996_Ul6xYxS.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "sayonara-wild-hearts",
            "name": "Sayonara Wild Hearts",
            "playtime": 2,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "iOS",
                        "slug": "ios"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "macOS",
                        "slug": "macos"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 4,
                        "name": "App Store",
                        "slug": "apple-appstore"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2019-09-19",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/77c/77ca75b962f0ca9f7de6eb03814d6b5b.jpg",
            "rating": 4.4,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 154,
                    "percent": 54.8
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 95,
                    "percent": 33.81
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 27,
                    "percent": 9.61
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 5,
                    "percent": 1.78
                }
            ],
            "ratings_count": 275,
            "reviews_text_count": 4,
            "added": 1033,
            "added_by_status": {
                "yet": 40,
                "owned": 488,
                "beaten": 285,
                "toplay": 165,
                "dropped": 37,
                "playing": 18
            },
            "metacritic": 85,
            "suggestions_count": 143,
            "updated": "2023-04-06T16:55:12",
            "id": 274757,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42399,
                    "name": "Казуальная игра",
                    "slug": "kazualnaia-igra",
                    "language": "rus",
                    "games_count": 30679,
                    "image_background": "https://media.rawg.io/media/games/e74/e74458058b35e01c1ae3feeb39a3f724.jpg"
                },
                {
                    "id": 42480,
                    "name": "Фэнтези",
                    "slug": "fentezi",
                    "language": "rus",
                    "games_count": 7813,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 64,
                    "name": "Fantasy",
                    "slug": "fantasy",
                    "language": "eng",
                    "games_count": 25175,
                    "image_background": "https://media.rawg.io/media/games/33d/33df5a032898b8ab7e3773c7a5f1d336.jpg"
                },
                {
                    "id": 189,
                    "name": "Female Protagonist",
                    "slug": "female-protagonist",
                    "language": "eng",
                    "games_count": 10677,
                    "image_background": "https://media.rawg.io/media/games/1fb/1fb1c5f7a71d771f440b27ce7f71e7eb.jpg"
                },
                {
                    "id": 42404,
                    "name": "Женщина-протагонист",
                    "slug": "zhenshchina-protagonist",
                    "language": "rus",
                    "games_count": 2416,
                    "image_background": "https://media.rawg.io/media/games/7f6/7f6cd70ba2ad57053b4847c13569f2d8.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42587,
                    "name": "Аркада",
                    "slug": "arkada",
                    "language": "rus",
                    "games_count": 7255,
                    "image_background": "https://media.rawg.io/media/games/a32/a32c9c299488ca99afc3fcea605a7718.jpg"
                },
                {
                    "id": 111,
                    "name": "Short",
                    "slug": "short",
                    "language": "eng",
                    "games_count": 61130,
                    "image_background": "https://media.rawg.io/media/games/7fa/7fa0b586293c5861ee32490e953a4996.jpg"
                },
                {
                    "id": 42457,
                    "name": "Короткая",
                    "slug": "korotkaia",
                    "language": "rus",
                    "games_count": 1308,
                    "image_background": "https://media.rawg.io/media/games/d5a/d5a24f9f71315427fa6e966fdd98dfa6.jpg"
                },
                {
                    "id": 42601,
                    "name": "Цветастая",
                    "slug": "tsvetastaia",
                    "language": "rus",
                    "games_count": 8716,
                    "image_background": "https://media.rawg.io/media/games/e74/e74458058b35e01c1ae3feeb39a3f724.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5545,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 165,
                    "name": "Colorful",
                    "slug": "colorful",
                    "language": "eng",
                    "games_count": 17830,
                    "image_background": "https://media.rawg.io/media/games/c2e/c2eb6021a2596644b437e943612af25c.jpg"
                },
                {
                    "id": 571,
                    "name": "3D",
                    "slug": "3d",
                    "language": "eng",
                    "games_count": 81983,
                    "image_background": "https://media.rawg.io/media/screenshots/066/066eb1b7a3f332b8089645fbf8c3ebdc.jpg"
                },
                {
                    "id": 42690,
                    "name": "Красивая",
                    "slug": "krasivaia",
                    "language": "rus",
                    "games_count": 537,
                    "image_background": "https://media.rawg.io/media/games/90c/90caf1fcb836cad70013452f6f239008.jpg"
                },
                {
                    "id": 136,
                    "name": "Music",
                    "slug": "music",
                    "language": "eng",
                    "games_count": 26820,
                    "image_background": "https://media.rawg.io/media/games/f99/f9979698c43fd84c3ab69280576dd3af.jpg"
                },
                {
                    "id": 42606,
                    "name": "Стилизация",
                    "slug": "stilizatsiia",
                    "language": "rus",
                    "games_count": 4002,
                    "image_background": "https://media.rawg.io/media/games/8cd/8cd179c85bd3de8f79bef245b15075fb.jpg"
                },
                {
                    "id": 166,
                    "name": "Stylized",
                    "slug": "stylized",
                    "language": "eng",
                    "games_count": 4026,
                    "image_background": "https://media.rawg.io/media/games/b6b/b6b20bfc4b34e312dbc8aac53c95a348.jpg"
                },
                {
                    "id": 42620,
                    "name": "Музыка",
                    "slug": "muzyka",
                    "language": "rus",
                    "games_count": 945,
                    "image_background": "https://media.rawg.io/media/screenshots/695/69511e8a8ec8edf9b85c3e68190844a4.jpg"
                },
                {
                    "id": 577,
                    "name": "Beautiful",
                    "slug": "beautiful",
                    "language": "eng",
                    "games_count": 1820,
                    "image_background": "https://media.rawg.io/media/games/d3e/d3ee2d7653cf9d4640335ff7a471ab07.jpg"
                },
                {
                    "id": 42410,
                    "name": "LGBTQ+",
                    "slug": "lgbtq-2",
                    "language": "eng",
                    "games_count": 1140,
                    "image_background": "https://media.rawg.io/media/screenshots/f37/f37a6ef6d58c92b21410861734d61c69.jpeg"
                },
                {
                    "id": 207,
                    "name": "Rhythm",
                    "slug": "rhythm",
                    "language": "eng",
                    "games_count": 1863,
                    "image_background": "https://media.rawg.io/media/screenshots/90f/90f61894908915eff8455e7b43d466a2.jpg"
                },
                {
                    "id": 42618,
                    "name": "Ритм-игра",
                    "slug": "ritm-igra",
                    "language": "rus",
                    "games_count": 725,
                    "image_background": "https://media.rawg.io/media/screenshots/ca9/ca95a5bb74f37b4a483a2e88ec604097.jpg"
                },
                {
                    "id": 43374,
                    "name": "Remote Play on TV",
                    "slug": "remote-play-on-tv",
                    "language": "eng",
                    "games_count": 312,
                    "image_background": "https://media.rawg.io/media/games/77c/77ca75b962f0ca9f7de6eb03814d6b5b.jpg"
                },
                {
                    "id": 974,
                    "name": "death",
                    "slug": "death",
                    "language": "eng",
                    "games_count": 3867,
                    "image_background": "https://media.rawg.io/media/games/f61/f61cc8e0bce08615d90918e428aa5dc9.jpg"
                },
                {
                    "id": 43578,
                    "name": "Remote Play on Tablet",
                    "slug": "remote-play-on-tablet",
                    "language": "eng",
                    "games_count": 145,
                    "image_background": "https://media.rawg.io/media/games/381/3811a1d23a58974a2cac2d757023e5de.jpg"
                },
                {
                    "id": 2889,
                    "name": "balance",
                    "slug": "balance",
                    "language": "eng",
                    "games_count": 1702,
                    "image_background": "https://media.rawg.io/media/games/f17/f17cb19c5e9b30e378e5f9ba1cc74df3.jpg"
                },
                {
                    "id": 43577,
                    "name": "Remote Play on Phone",
                    "slug": "remote-play-on-phone",
                    "language": "eng",
                    "games_count": 140,
                    "image_background": "https://media.rawg.io/media/screenshots/daf/daf4b6886e6dc5eb50a00f3a30bec6c3.jpg"
                },
                {
                    "id": 657,
                    "name": "Dreams",
                    "slug": "dreams",
                    "language": "eng",
                    "games_count": 2576,
                    "image_background": "https://media.rawg.io/media/games/6f9/6f932bffab5e38f540e10bb026621b08.jpg"
                },
                {
                    "id": 2406,
                    "name": "dance",
                    "slug": "dance",
                    "language": "eng",
                    "games_count": 1186,
                    "image_background": "https://media.rawg.io/media/screenshots/f41/f4145c17b374272b3c7e0ed42a91e7cc.jpg"
                },
                {
                    "id": 835,
                    "name": "Swords",
                    "slug": "swords",
                    "language": "eng",
                    "games_count": 1534,
                    "image_background": "https://media.rawg.io/media/games/3e5/3e56242579cba53b1eeeca52571b3423.jpg"
                },
                {
                    "id": 3654,
                    "name": "lasers",
                    "slug": "lasers",
                    "language": "eng",
                    "games_count": 765,
                    "image_background": "https://media.rawg.io/media/screenshots/5bb/5bbd71548240703f3bc42cee7c87972d.jpg"
                }
            ],
            "esrb_rating": {
                "id": 2,
                "name": "Everyone 10+",
                "slug": "everyone-10-plus",
                "name_en": "Everyone 10+",
                "name_ru": "С 10 лет"
            },
            "user_game": None,
            "reviews_count": 281,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/77c/77ca75b962f0ca9f7de6eb03814d6b5b.jpg"
                },
                {
                    "id": 1767945,
                    "image": "https://media.rawg.io/media/screenshots/5e7/5e70f3418fa74dbd8a8787e6f8e0e4be.jpg"
                },
                {
                    "id": 1767946,
                    "image": "https://media.rawg.io/media/screenshots/f13/f13adb07eccf4956ecd6a91a84f9be08.jpg"
                },
                {
                    "id": 1767947,
                    "image": "https://media.rawg.io/media/screenshots/e32/e32a42b305924f991468e63dd714ca02.jpeg"
                },
                {
                    "id": 1767948,
                    "image": "https://media.rawg.io/media/screenshots/35a/35a8889375a92b8b7a3d15fd7791203e.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 4,
                        "name": "iOS",
                        "slug": "ios"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "Apple Macintosh",
                        "slug": "mac"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 40,
                    "name": "Casual",
                    "slug": "casual"
                },
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "neon-white",
            "name": "Neon White",
            "playtime": 6,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2022-06-16",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/a12/a120fc7faed7666f8c320a755137e316.jpg",
            "rating": 4.4,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 63,
                    "percent": 55.75
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 42,
                    "percent": 37.17
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 5,
                    "percent": 4.42
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 3,
                    "percent": 2.65
                }
            ],
            "ratings_count": 111,
            "reviews_text_count": 1,
            "added": 951,
            "added_by_status": {
                "yet": 66,
                "owned": 572,
                "beaten": 87,
                "toplay": 166,
                "dropped": 31,
                "playing": 29
            },
            "metacritic": 88,
            "suggestions_count": 236,
            "updated": "2023-04-12T12:04:21",
            "id": 558980,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42428,
                    "name": "Шутер",
                    "slug": "shuter",
                    "language": "rus",
                    "games_count": 6479,
                    "image_background": "https://media.rawg.io/media/games/c24/c24ec439abf4a2e92f3429dfa83f7f94.jpg"
                },
                {
                    "id": 8,
                    "name": "First-Person",
                    "slug": "first-person",
                    "language": "eng",
                    "games_count": 29966,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 30,
                    "name": "FPS",
                    "slug": "fps",
                    "language": "eng",
                    "games_count": 12754,
                    "image_background": "https://media.rawg.io/media/games/f87/f87457e8347484033cb34cde6101d08d.jpg"
                },
                {
                    "id": 42427,
                    "name": "Шутер от первого лица",
                    "slug": "shuter-ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 3952,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 40850,
                    "name": "Steam Leaderboards",
                    "slug": "steam-leaderboards",
                    "language": "eng",
                    "games_count": 5753,
                    "image_background": "https://media.rawg.io/media/games/59a/59a3ebcba3d08c51532c6ca877aff256.jpg"
                },
                {
                    "id": 42463,
                    "name": "Платформер",
                    "slug": "platformer-2",
                    "language": "rus",
                    "games_count": 6297,
                    "image_background": "https://media.rawg.io/media/games/89a/89a700d3c6a76bd0610ca89ccd20da54.jpg"
                },
                {
                    "id": 134,
                    "name": "Anime",
                    "slug": "anime",
                    "language": "eng",
                    "games_count": 11173,
                    "image_background": "https://media.rawg.io/media/games/cc5/cc576aa274780702ef93463f5410031e.jpg"
                },
                {
                    "id": 42407,
                    "name": "Аниме",
                    "slug": "anime-2",
                    "language": "rus",
                    "games_count": 6641,
                    "image_background": "https://media.rawg.io/media/games/a38/a3857b2445c70ac5dbe73b210a827ad8.jpg"
                },
                {
                    "id": 42556,
                    "name": "Тайна",
                    "slug": "taina",
                    "language": "rus",
                    "games_count": 3559,
                    "image_background": "https://media.rawg.io/media/games/948/948fe7f00b6cba8472f5ecd07a455077.jpg"
                },
                {
                    "id": 117,
                    "name": "Mystery",
                    "slug": "mystery",
                    "language": "eng",
                    "games_count": 12105,
                    "image_background": "https://media.rawg.io/media/screenshots/9d2/9d22689a1c2a7ced9d1690e0c5c66871.jpg"
                },
                {
                    "id": 42643,
                    "name": "Паркур",
                    "slug": "parkur-2",
                    "language": "rus",
                    "games_count": 787,
                    "image_background": "https://media.rawg.io/media/games/74d/74dafeb9a442b87b9dd4a1d4a2faa37b.jpg"
                },
                {
                    "id": 188,
                    "name": "Parkour",
                    "slug": "parkour",
                    "language": "eng",
                    "games_count": 3349,
                    "image_background": "https://media.rawg.io/media/games/4a5/4a5ce21f529cf8fd4670b4c3188b25df.jpg"
                },
                {
                    "id": 571,
                    "name": "3D",
                    "slug": "3d",
                    "language": "eng",
                    "games_count": 81983,
                    "image_background": "https://media.rawg.io/media/screenshots/066/066eb1b7a3f332b8089645fbf8c3ebdc.jpg"
                },
                {
                    "id": 42393,
                    "name": "Визуальная новелла",
                    "slug": "vizualnaia-novella",
                    "language": "rus",
                    "games_count": 4674,
                    "image_background": "https://media.rawg.io/media/games/01a/01a74b440fba4dce445cc2ff11b99220.jpg"
                },
                {
                    "id": 90,
                    "name": "Visual Novel",
                    "slug": "visual-novel",
                    "language": "eng",
                    "games_count": 4506,
                    "image_background": "https://media.rawg.io/media/games/972/972aea3c9eb253e893947bec2d2cfbb9.jpg"
                },
                {
                    "id": 42494,
                    "name": "3D-платформер",
                    "slug": "3d-platformer-2",
                    "language": "rus",
                    "games_count": 2558,
                    "image_background": "https://media.rawg.io/media/games/74d/74dafeb9a442b87b9dd4a1d4a2faa37b.jpg"
                },
                {
                    "id": 42606,
                    "name": "Стилизация",
                    "slug": "stilizatsiia",
                    "language": "rus",
                    "games_count": 4002,
                    "image_background": "https://media.rawg.io/media/games/8cd/8cd179c85bd3de8f79bef245b15075fb.jpg"
                },
                {
                    "id": 166,
                    "name": "Stylized",
                    "slug": "stylized",
                    "language": "eng",
                    "games_count": 4026,
                    "image_background": "https://media.rawg.io/media/games/b6b/b6b20bfc4b34e312dbc8aac53c95a348.jpg"
                },
                {
                    "id": 229,
                    "name": "3D Platformer",
                    "slug": "3d-platformer",
                    "language": "eng",
                    "games_count": 8988,
                    "image_background": "https://media.rawg.io/media/screenshots/57f/57f97397220442e71c51f9ba44b67fec_KzipzFC.jpeg"
                },
                {
                    "id": 42408,
                    "name": "Симулятор свиданий",
                    "slug": "simuliator-svidanii",
                    "language": "rus",
                    "games_count": 1780,
                    "image_background": "https://media.rawg.io/media/games/345/34589f72fe291f0f38f12488f28c8f43.jpg"
                },
                {
                    "id": 42627,
                    "name": "Повествование",
                    "slug": "povestvovanie",
                    "language": "rus",
                    "games_count": 465,
                    "image_background": "https://media.rawg.io/media/games/6c8/6c8cb4780ce30b76b944cf656e8fff49.jpg"
                },
                {
                    "id": 160,
                    "name": "Dating Sim",
                    "slug": "dating-sim",
                    "language": "eng",
                    "games_count": 4400,
                    "image_background": "https://media.rawg.io/media/games/713/713269608dc8f2f40f5a670a14b2de94.jpg"
                },
                {
                    "id": 583,
                    "name": "Narrative",
                    "slug": "narrative",
                    "language": "eng",
                    "games_count": 9112,
                    "image_background": "https://media.rawg.io/media/screenshots/3ee/3eea6a5902e15c59c8b503d7f8cb07f6.jpg"
                },
                {
                    "id": 49963,
                    "name": "Precision Platformer",
                    "slug": "precision-platformer-2",
                    "language": "eng",
                    "games_count": 1157,
                    "image_background": "https://media.rawg.io/media/screenshots/b74/b7464eefc41129a08eef62b3049a7544.jpg"
                },
                {
                    "id": 49999,
                    "name": "Платформер на точность",
                    "slug": "platformer-na-tochnost",
                    "language": "rus",
                    "games_count": 1144,
                    "image_background": "https://media.rawg.io/media/screenshots/d27/d27e40c278164b4b1874b1354402396f.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 113,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/a12/a120fc7faed7666f8c320a755137e316.jpg"
                },
                {
                    "id": 2717687,
                    "image": "https://media.rawg.io/media/screenshots/d80/d80f355d433a4c3e65c03f895cce13fb.jpg"
                },
                {
                    "id": 2717688,
                    "image": "https://media.rawg.io/media/screenshots/a7f/a7f382410a233f33878f8ba889507424.jpg"
                },
                {
                    "id": 2717689,
                    "image": "https://media.rawg.io/media/screenshots/e4e/e4e6e0e28de770d8a7741848772a5bc7.jpg"
                },
                {
                    "id": 2717690,
                    "image": "https://media.rawg.io/media/screenshots/64b/64bd9f163c7e793c79f1df68bccab021.jpg"
                },
                {
                    "id": 2717691,
                    "image": "https://media.rawg.io/media/screenshots/9af/9af75d8e658125b90f9cf3d96d434ae5.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 2,
                    "name": "Shooter",
                    "slug": "shooter"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "elden-ring",
            "name": "Elden Ring",
            "playtime": 57,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2022-02-25",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/5ec/5ecac5cb026ec26a56efcc546364e348.jpg",
            "rating": 4.4,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 553,
                    "percent": 66.63
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 159,
                    "percent": 19.16
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 65,
                    "percent": 7.83
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 53,
                    "percent": 6.39
                }
            ],
            "ratings_count": 799,
            "reviews_text_count": 22,
            "added": 5697,
            "added_by_status": {
                "yet": 298,
                "owned": 3550,
                "beaten": 558,
                "toplay": 823,
                "dropped": 208,
                "playing": 260
            },
            "metacritic": 95,
            "suggestions_count": 559,
            "updated": "2023-04-16T13:38:11",
            "id": 326243,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 24,
                    "name": "RPG",
                    "slug": "rpg",
                    "language": "eng",
                    "games_count": 17009,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 18,
                    "name": "Co-op",
                    "slug": "co-op",
                    "language": "eng",
                    "games_count": 9806,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 42412,
                    "name": "Ролевая игра",
                    "slug": "rolevaia-igra",
                    "language": "rus",
                    "games_count": 13302,
                    "image_background": "https://media.rawg.io/media/games/ee3/ee3e10193aafc3230ba1cae426967d10.jpg"
                },
                {
                    "id": 42442,
                    "name": "Открытый мир",
                    "slug": "otkrytyi-mir",
                    "language": "rus",
                    "games_count": 4297,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 411,
                    "name": "cooperative",
                    "slug": "cooperative",
                    "language": "eng",
                    "games_count": 3973,
                    "image_background": "https://media.rawg.io/media/games/baf/baf9905270314e07e6850cffdb51df41.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 42420,
                    "name": "Сложная",
                    "slug": "slozhnaia",
                    "language": "rus",
                    "games_count": 4385,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 9,
                    "name": "Online Co-Op",
                    "slug": "online-co-op",
                    "language": "eng",
                    "games_count": 4246,
                    "image_background": "https://media.rawg.io/media/games/d69/d69810315bd7e226ea2d21f9156af629.jpg"
                },
                {
                    "id": 42480,
                    "name": "Фэнтези",
                    "slug": "fentezi",
                    "language": "rus",
                    "games_count": 7813,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 64,
                    "name": "Fantasy",
                    "slug": "fantasy",
                    "language": "eng",
                    "games_count": 25175,
                    "image_background": "https://media.rawg.io/media/games/33d/33df5a032898b8ab7e3773c7a5f1d336.jpg"
                },
                {
                    "id": 49,
                    "name": "Difficult",
                    "slug": "difficult",
                    "language": "eng",
                    "games_count": 13060,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 97,
                    "name": "Action RPG",
                    "slug": "action-rpg",
                    "language": "eng",
                    "games_count": 5874,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 42489,
                    "name": "Ролевой экшен",
                    "slug": "rolevoi-ekshen",
                    "language": "rus",
                    "games_count": 2557,
                    "image_background": "https://media.rawg.io/media/games/5be/5bec14622f6faf804a592176577c1347.jpg"
                },
                {
                    "id": 157,
                    "name": "PvP",
                    "slug": "pvp",
                    "language": "eng",
                    "games_count": 7102,
                    "image_background": "https://media.rawg.io/media/games/9c4/9c47f320eb73c9a02d462e12f6206b26.jpg"
                },
                {
                    "id": 42434,
                    "name": "Игрок против игрока",
                    "slug": "igrok-protiv-igroka",
                    "language": "rus",
                    "games_count": 3392,
                    "image_background": "https://media.rawg.io/media/games/9af/9af24c1886e2c7b52a4a2c65aa874638.jpg"
                },
                {
                    "id": 42506,
                    "name": "Тёмное фэнтези",
                    "slug": "tiomnoe-fentezi",
                    "language": "rus",
                    "games_count": 1830,
                    "image_background": "https://media.rawg.io/media/games/cfe/cfe5960b5caca432f3575fc7d8ff736b.jpg"
                },
                {
                    "id": 40,
                    "name": "Dark Fantasy",
                    "slug": "dark-fantasy",
                    "language": "eng",
                    "games_count": 3255,
                    "image_background": "https://media.rawg.io/media/games/501/501e7019925a3c692bf1c8062f07abe6.jpg"
                },
                {
                    "id": 42555,
                    "name": "Симулятор ходьбы",
                    "slug": "simuliator-khodby",
                    "language": "rus",
                    "games_count": 1717,
                    "image_background": "https://media.rawg.io/media/screenshots/8f0/8f0b94922ad5e59968852649697b2643.jpg"
                },
                {
                    "id": 42564,
                    "name": "Расслабляющая",
                    "slug": "rasslabliaiushchaia",
                    "language": "rus",
                    "games_count": 5737,
                    "image_background": "https://media.rawg.io/media/games/5aa/5aa4c12a53bc5f606bf8d92461ec747d.jpg"
                },
                {
                    "id": 571,
                    "name": "3D",
                    "slug": "3d",
                    "language": "eng",
                    "games_count": 81983,
                    "image_background": "https://media.rawg.io/media/screenshots/066/066eb1b7a3f332b8089645fbf8c3ebdc.jpg"
                },
                {
                    "id": 45878,
                    "name": "Online PvP",
                    "slug": "online-pvp",
                    "language": "eng",
                    "games_count": 3021,
                    "image_background": "https://media.rawg.io/media/games/c3b/c3be1d5f55cb9324c97ccb7aaaf42ad4.jpg"
                },
                {
                    "id": 40937,
                    "name": "Steam Trading Cards",
                    "slug": "steam-trading-cards-2",
                    "language": "eng",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 42592,
                    "name": "Похожа на Dark Souls",
                    "slug": "pokhozha-na-dark-souls",
                    "language": "rus",
                    "games_count": 605,
                    "image_background": "https://media.rawg.io/media/games/718/71891d2484a592d871e91dc826707e1c.jpg"
                },
                {
                    "id": 581,
                    "name": "Epic",
                    "slug": "epic",
                    "language": "eng",
                    "games_count": 4127,
                    "image_background": "https://media.rawg.io/media/games/5ec/5ecac5cb026ec26a56efcc546364e348.jpg"
                },
                {
                    "id": 58132,
                    "name": "Атмосферная",
                    "slug": "atmosfernaia",
                    "language": "rus",
                    "games_count": 4619,
                    "image_background": "https://media.rawg.io/media/games/044/044b2ee023930ca138deda151f40c18c.jpg"
                },
                {
                    "id": 580,
                    "name": "Souls-like",
                    "slug": "souls-like",
                    "language": "eng",
                    "games_count": 1032,
                    "image_background": "https://media.rawg.io/media/games/043/043f8b4a5d9b767694370d6fbbc8cd3c.jpg"
                },
                {
                    "id": 70351,
                    "name": "Сетевой кооператив",
                    "slug": "setevoi-kooperativ",
                    "language": "rus",
                    "games_count": 810,
                    "image_background": "https://media.rawg.io/media/screenshots/6ab/6abb5456a795b7713919db7568a2fd96.jpg"
                },
                {
                    "id": 1221,
                    "name": "history",
                    "slug": "history",
                    "language": "eng",
                    "games_count": 2364,
                    "image_background": "https://media.rawg.io/media/screenshots/474/47478ccb205e4e0d0117986107625599.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 830,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/5ec/5ecac5cb026ec26a56efcc546364e348.jpg"
                },
                {
                    "id": 2877235,
                    "image": "https://media.rawg.io/media/screenshots/36f/36f941f72e2b2a41629f5fb3bd448688.jpg"
                },
                {
                    "id": 2877236,
                    "image": "https://media.rawg.io/media/screenshots/290/29096848622521df7555850000236cb6.jpg"
                },
                {
                    "id": 2877237,
                    "image": "https://media.rawg.io/media/screenshots/807/807685454ea8fb87363eedd49677f49b.jpg"
                },
                {
                    "id": 2877238,
                    "image": "https://media.rawg.io/media/screenshots/2ee/2eea4d4cce2836f689d9d39d2a4a94d5.jpg"
                },
                {
                    "id": 2877239,
                    "image": "https://media.rawg.io/media/screenshots/de9/de9b28bdd0bdb9937c7f82e55f845bb6.jpg"
                },
                {
                    "id": 2877240,
                    "image": "https://media.rawg.io/media/screenshots/3a2/3a2e5f31e2061bc566bcfd30fda56a17.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "half-life-alyx",
            "name": "Half-Life: Alyx",
            "playtime": 5,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                }
            ],
            "released": "2020-03-23",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/855/8552c056d729f34c951c30f3cfef9da8.jpg",
            "rating": 4.39,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 245,
                    "percent": 66.94
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 76,
                    "percent": 20.77
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 29,
                    "percent": 7.92
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 16,
                    "percent": 4.37
                }
            ],
            "ratings_count": 358,
            "reviews_text_count": 6,
            "added": 2489,
            "added_by_status": {
                "yet": 191,
                "owned": 1354,
                "beaten": 203,
                "toplay": 591,
                "dropped": 60,
                "playing": 90
            },
            "metacritic": 93,
            "suggestions_count": 540,
            "updated": "2023-04-16T07:21:26",
            "id": 392019,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42428,
                    "name": "Шутер",
                    "slug": "shuter",
                    "language": "rus",
                    "games_count": 6479,
                    "image_background": "https://media.rawg.io/media/games/c24/c24ec439abf4a2e92f3429dfa83f7f94.jpg"
                },
                {
                    "id": 8,
                    "name": "First-Person",
                    "slug": "first-person",
                    "language": "eng",
                    "games_count": 29966,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 42435,
                    "name": "Шедевр",
                    "slug": "shedevr",
                    "language": "rus",
                    "games_count": 1059,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 32,
                    "name": "Sci-fi",
                    "slug": "sci-fi",
                    "language": "eng",
                    "games_count": 17671,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42423,
                    "name": "Научная фантастика",
                    "slug": "nauchnaia-fantastika",
                    "language": "rus",
                    "games_count": 5796,
                    "image_background": "https://media.rawg.io/media/games/3cf/3cff89996570cf29a10eb9cd967dcf73.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 30,
                    "name": "FPS",
                    "slug": "fps",
                    "language": "eng",
                    "games_count": 12754,
                    "image_background": "https://media.rawg.io/media/games/f87/f87457e8347484033cb34cde6101d08d.jpg"
                },
                {
                    "id": 42427,
                    "name": "Шутер от первого лица",
                    "slug": "shuter-ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 3952,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 189,
                    "name": "Female Protagonist",
                    "slug": "female-protagonist",
                    "language": "eng",
                    "games_count": 10677,
                    "image_background": "https://media.rawg.io/media/games/1fb/1fb1c5f7a71d771f440b27ce7f71e7eb.jpg"
                },
                {
                    "id": 42404,
                    "name": "Женщина-протагонист",
                    "slug": "zhenshchina-protagonist",
                    "language": "rus",
                    "games_count": 2416,
                    "image_background": "https://media.rawg.io/media/games/7f6/7f6cd70ba2ad57053b4847c13569f2d8.jpg"
                },
                {
                    "id": 40852,
                    "name": "Steam Workshop",
                    "slug": "steam-workshop",
                    "language": "eng",
                    "games_count": 1287,
                    "image_background": "https://media.rawg.io/media/games/9bf/9bfac18ff678f41a4674250fa0e04a52.jpg"
                },
                {
                    "id": 63,
                    "name": "Zombies",
                    "slug": "zombies",
                    "language": "eng",
                    "games_count": 10130,
                    "image_background": "https://media.rawg.io/media/games/d64/d646810b629081cc12aec49ed9f49441.jpg"
                },
                {
                    "id": 40838,
                    "name": "Includes level editor",
                    "slug": "includes-level-editor",
                    "language": "eng",
                    "games_count": 1613,
                    "image_background": "https://media.rawg.io/media/games/054/0549f1a0a5e782d4e81cdf8d022073fa.jpg"
                },
                {
                    "id": 42544,
                    "name": "Зомби",
                    "slug": "zombi-2",
                    "language": "rus",
                    "games_count": 1929,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 40833,
                    "name": "Captions available",
                    "slug": "captions-available",
                    "language": "eng",
                    "games_count": 1221,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 167,
                    "name": "Futuristic",
                    "slug": "futuristic",
                    "language": "eng",
                    "games_count": 4314,
                    "image_background": "https://media.rawg.io/media/games/b7d/b7d3f1715fa8381a4e780173a197a615.jpg"
                },
                {
                    "id": 120,
                    "name": "Memes",
                    "slug": "memes",
                    "language": "eng",
                    "games_count": 1573,
                    "image_background": "https://media.rawg.io/media/games/bce/bce62fbc7cf74bf6a1a37340993ec148.jpg"
                },
                {
                    "id": 172,
                    "name": "Aliens",
                    "slug": "aliens",
                    "language": "eng",
                    "games_count": 6441,
                    "image_background": "https://media.rawg.io/media/games/34b/34b1f1850a1c06fd971bc6ab3ac0ce0e.jpg"
                },
                {
                    "id": 42561,
                    "name": "Мемы",
                    "slug": "memy",
                    "language": "rus",
                    "games_count": 1387,
                    "image_background": "https://media.rawg.io/media/games/11f/11fd681c312c14644ab360888dba3486.jpg"
                },
                {
                    "id": 33,
                    "name": "VR",
                    "slug": "vr",
                    "language": "eng",
                    "games_count": 11800,
                    "image_background": "https://media.rawg.io/media/screenshots/c02/c02c64324edc2045ea1fc0601cdaaa0c.jpg"
                },
                {
                    "id": 42451,
                    "name": "Будущее",
                    "slug": "budushchee",
                    "language": "rus",
                    "games_count": 2342,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42485,
                    "name": "Инопланетяне",
                    "slug": "inoplanetiane",
                    "language": "rus",
                    "games_count": 1258,
                    "image_background": "https://media.rawg.io/media/games/c24/c24f4434882ae9c2c8d9d38de82cb7a5.jpg"
                },
                {
                    "id": 42690,
                    "name": "Красивая",
                    "slug": "krasivaia",
                    "language": "rus",
                    "games_count": 537,
                    "image_background": "https://media.rawg.io/media/games/90c/90caf1fcb836cad70013452f6f239008.jpg"
                },
                {
                    "id": 578,
                    "name": "Masterpiece",
                    "slug": "masterpiece",
                    "language": "eng",
                    "games_count": 276,
                    "image_background": "https://media.rawg.io/media/games/0fa/0fa9e2b8397b332902d3b56c73888d52.jpg"
                },
                {
                    "id": 577,
                    "name": "Beautiful",
                    "slug": "beautiful",
                    "language": "eng",
                    "games_count": 1820,
                    "image_background": "https://media.rawg.io/media/games/d3e/d3ee2d7653cf9d4640335ff7a471ab07.jpg"
                },
                {
                    "id": 40938,
                    "name": "VR Support",
                    "slug": "vr-support-2",
                    "language": "eng",
                    "games_count": 14,
                    "image_background": "https://media.rawg.io/media/screenshots/1fb/1fb71741fbae309c0aed4514fedcb7a6.jpg"
                },
                {
                    "id": 885,
                    "name": "vive",
                    "slug": "vive",
                    "language": "eng",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/screenshots/2af/2af65707ec97c255df46ba727792e5c3.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 366,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/855/8552c056d729f34c951c30f3cfef9da8.jpg"
                },
                {
                    "id": 2236546,
                    "image": "https://media.rawg.io/media/screenshots/4af/4af359175bfb080eac07d076233cdadc.jpg"
                },
                {
                    "id": 2236547,
                    "image": "https://media.rawg.io/media/screenshots/0e9/0e9cc635f41896855a907737fa99310e.jpg"
                },
                {
                    "id": 2236548,
                    "image": "https://media.rawg.io/media/screenshots/d75/d753ab1d6cfe577faf62adc87d8338b4.jpg"
                },
                {
                    "id": 2236549,
                    "image": "https://media.rawg.io/media/screenshots/90d/90db6c35af854f27f0abf4cc1643eea6.jpg"
                },
                {
                    "id": 2236550,
                    "image": "https://media.rawg.io/media/screenshots/303/30371caa4d754f66993ef9ab84f95456.jpg"
                },
                {
                    "id": 2236551,
                    "image": "https://media.rawg.io/media/screenshots/9d9/9d9d4e5383bc10784ca4db96379269f9.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                }
            ],
            "genres": [
                {
                    "id": 2,
                    "name": "Shooter",
                    "slug": "shooter"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "resident-evil-village",
            "name": "Resident Evil: Village",
            "playtime": 16,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2021-05-07",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/6cc/6cc23249972a427f697a3d10eb57a820.jpg",
            "rating": 4.39,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 410,
                    "percent": 55.48
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 258,
                    "percent": 34.91
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 46,
                    "percent": 6.22
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 25,
                    "percent": 3.38
                }
            ],
            "ratings_count": 712,
            "reviews_text_count": 18,
            "added": 3901,
            "added_by_status": {
                "yet": 252,
                "owned": 2181,
                "beaten": 790,
                "toplay": 570,
                "dropped": 58,
                "playing": 50
            },
            "metacritic": 83,
            "suggestions_count": 834,
            "updated": "2023-04-16T05:05:21",
            "id": 452649,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42442,
                    "name": "Открытый мир",
                    "slug": "otkrytyi-mir",
                    "language": "rus",
                    "games_count": 4297,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 8,
                    "name": "First-Person",
                    "slug": "first-person",
                    "language": "eng",
                    "games_count": 29966,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 30,
                    "name": "FPS",
                    "slug": "fps",
                    "language": "eng",
                    "games_count": 12754,
                    "image_background": "https://media.rawg.io/media/games/f87/f87457e8347484033cb34cde6101d08d.jpg"
                },
                {
                    "id": 42427,
                    "name": "Шутер от первого лица",
                    "slug": "shuter-ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 3952,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42491,
                    "name": "Мясо",
                    "slug": "miaso",
                    "language": "rus",
                    "games_count": 3850,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 26,
                    "name": "Gore",
                    "slug": "gore",
                    "language": "eng",
                    "games_count": 5083,
                    "image_background": "https://media.rawg.io/media/games/998/9980c4296f311d8bcc5b451ca51e4fe1.jpg"
                },
                {
                    "id": 1,
                    "name": "Survival",
                    "slug": "survival",
                    "language": "eng",
                    "games_count": 7130,
                    "image_background": "https://media.rawg.io/media/games/d7d/d7d33daa1892e2468cd0263d5dfc957e.jpg"
                },
                {
                    "id": 42452,
                    "name": "Выживание",
                    "slug": "vyzhivanie",
                    "language": "rus",
                    "games_count": 4550,
                    "image_background": "https://media.rawg.io/media/games/daa/daaee07fcb40744d90cf8142f94a241f.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 42477,
                    "name": "Мрачная",
                    "slug": "mrachnaia",
                    "language": "rus",
                    "games_count": 3416,
                    "image_background": "https://media.rawg.io/media/games/d9f/d9f982e042df6263684ba1fdea3efc1c.jpg"
                },
                {
                    "id": 41,
                    "name": "Dark",
                    "slug": "dark",
                    "language": "eng",
                    "games_count": 14620,
                    "image_background": "https://media.rawg.io/media/games/ffe/ffed87105b14f5beff72ff44a7793fd5.jpg"
                },
                {
                    "id": 42406,
                    "name": "Нагота",
                    "slug": "nagota",
                    "language": "rus",
                    "games_count": 4399,
                    "image_background": "https://media.rawg.io/media/games/a0e/a0ef08621301a1eab5e04fa5c96978fa.jpeg"
                },
                {
                    "id": 63,
                    "name": "Zombies",
                    "slug": "zombies",
                    "language": "eng",
                    "games_count": 10130,
                    "image_background": "https://media.rawg.io/media/games/d64/d646810b629081cc12aec49ed9f49441.jpg"
                },
                {
                    "id": 44,
                    "name": "Nudity",
                    "slug": "nudity",
                    "language": "eng",
                    "games_count": 4792,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 42544,
                    "name": "Зомби",
                    "slug": "zombi-2",
                    "language": "rus",
                    "games_count": 1929,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42471,
                    "name": "Хоррор на выживание",
                    "slug": "khorror-na-vyzhivanie",
                    "language": "rus",
                    "games_count": 2127,
                    "image_background": "https://media.rawg.io/media/games/447/4470c1e76f01acfaf5af9c207d1c1c92.jpg"
                },
                {
                    "id": 17,
                    "name": "Survival Horror",
                    "slug": "survival-horror",
                    "language": "eng",
                    "games_count": 8163,
                    "image_background": "https://media.rawg.io/media/games/b54/b54598d1d5cc31899f4f0a7e3122a7b0.jpg"
                },
                {
                    "id": 42405,
                    "name": "Сексуальный контент",
                    "slug": "seksualnyi-kontent",
                    "language": "rus",
                    "games_count": 4374,
                    "image_background": "https://media.rawg.io/media/games/df9/df988191048e92cf86dabd2987c47b62.jpg"
                },
                {
                    "id": 50,
                    "name": "Sexual Content",
                    "slug": "sexual-content",
                    "language": "eng",
                    "games_count": 4395,
                    "image_background": "https://media.rawg.io/media/games/522/522f66c5f8542a945b9e2b1942f1ad63.jpg"
                },
                {
                    "id": 40937,
                    "name": "Steam Trading Cards",
                    "slug": "steam-trading-cards-2",
                    "language": "eng",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 42408,
                    "name": "Симулятор свиданий",
                    "slug": "simuliator-svidanii",
                    "language": "rus",
                    "games_count": 1780,
                    "image_background": "https://media.rawg.io/media/games/345/34589f72fe291f0f38f12488f28c8f43.jpg"
                },
                {
                    "id": 160,
                    "name": "Dating Sim",
                    "slug": "dating-sim",
                    "language": "eng",
                    "games_count": 4400,
                    "image_background": "https://media.rawg.io/media/games/713/713269608dc8f2f40f5a670a14b2de94.jpg"
                },
                {
                    "id": 3103,
                    "name": "evil",
                    "slug": "evil",
                    "language": "eng",
                    "games_count": 1342,
                    "image_background": "https://media.rawg.io/media/games/40b/40b894b07c4f8b30c4324361490d3c0b.jpg"
                }
            ],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 739,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/6cc/6cc23249972a427f697a3d10eb57a820.jpg"
                },
                {
                    "id": 2796969,
                    "image": "https://media.rawg.io/media/screenshots/278/27848db6aeab58d7db5d33fe91722365.jpg"
                },
                {
                    "id": 2796970,
                    "image": "https://media.rawg.io/media/screenshots/456/4567bcc213eb9cede4acf9fc483f67a8.jpg"
                },
                {
                    "id": 2796971,
                    "image": "https://media.rawg.io/media/screenshots/121/121886081065b3b2124c917f70ff9659.jpg"
                },
                {
                    "id": 2796972,
                    "image": "https://media.rawg.io/media/screenshots/2ef/2ef1a6c044a2877cdb170a125f97bb97.jpg"
                },
                {
                    "id": 2796973,
                    "image": "https://media.rawg.io/media/screenshots/9b5/9b54295cadb720c76bc7999e94b17ebd.jpg"
                },
                {
                    "id": 2796974,
                    "image": "https://media.rawg.io/media/screenshots/221/221300277ed18c035c6b7aa0a9598f3e.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "little-nightmares-ii",
            "name": "Little Nightmares II",
            "playtime": 6,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 5,
                        "name": "GOG",
                        "slug": "gog"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2021-02-10",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/c2a/c2a7dc4540eb79aaff7099ae691105d3.jpg",
            "rating": 4.38,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 217,
                    "percent": 52.54
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 163,
                    "percent": 39.47
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 20,
                    "percent": 4.84
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 13,
                    "percent": 3.15
                }
            ],
            "ratings_count": 396,
            "reviews_text_count": 15,
            "added": 2013,
            "added_by_status": {
                "yet": 203,
                "owned": 809,
                "beaten": 420,
                "toplay": 500,
                "dropped": 51,
                "playing": 30
            },
            "metacritic": 82,
            "suggestions_count": 331,
            "updated": "2023-04-15T20:24:36",
            "id": 366881,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 42465,
                    "name": "Головоломка",
                    "slug": "golovolomka",
                    "language": "rus",
                    "games_count": 11084,
                    "image_background": "https://media.rawg.io/media/games/021/021c4e21a1824d2526f925eff6324653.jpg"
                },
                {
                    "id": 42463,
                    "name": "Платформер",
                    "slug": "platformer-2",
                    "language": "rus",
                    "games_count": 6297,
                    "image_background": "https://media.rawg.io/media/games/89a/89a700d3c6a76bd0610ca89ccd20da54.jpg"
                },
                {
                    "id": 15,
                    "name": "Stealth",
                    "slug": "stealth",
                    "language": "eng",
                    "games_count": 5846,
                    "image_background": "https://media.rawg.io/media/games/16b/16b1b7b36e2042d1128d5a3e852b3b2f.jpg"
                },
                {
                    "id": 42439,
                    "name": "Стелс",
                    "slug": "stels",
                    "language": "rus",
                    "games_count": 1510,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42477,
                    "name": "Мрачная",
                    "slug": "mrachnaia",
                    "language": "rus",
                    "games_count": 3416,
                    "image_background": "https://media.rawg.io/media/games/d9f/d9f982e042df6263684ba1fdea3efc1c.jpg"
                },
                {
                    "id": 41,
                    "name": "Dark",
                    "slug": "dark",
                    "language": "eng",
                    "games_count": 14620,
                    "image_background": "https://media.rawg.io/media/games/ffe/ffed87105b14f5beff72ff44a7793fd5.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5545,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 42468,
                    "name": "Головоломка-платформер",
                    "slug": "golovolomka-platformer",
                    "language": "rus",
                    "games_count": 2689,
                    "image_background": "https://media.rawg.io/media/games/ba0/ba006ef12175ad4773e5964c320099c4.jpg"
                },
                {
                    "id": 40937,
                    "name": "Steam Trading Cards",
                    "slug": "steam-trading-cards-2",
                    "language": "eng",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 42513,
                    "name": "Триллер",
                    "slug": "triller",
                    "language": "rus",
                    "games_count": 893,
                    "image_background": "https://media.rawg.io/media/games/c2a/c2a7dc4540eb79aaff7099ae691105d3.jpg"
                },
                {
                    "id": 183,
                    "name": "Thriller",
                    "slug": "thriller",
                    "language": "eng",
                    "games_count": 1973,
                    "image_background": "https://media.rawg.io/media/games/4c0/4c00f2f0436cde8c5eaecbf7607aff7c.jpg"
                },
                {
                    "id": 49955,
                    "name": "Puzzle Platformer",
                    "slug": "puzzle-platformer-2",
                    "language": "eng",
                    "games_count": 1974,
                    "image_background": "https://media.rawg.io/media/screenshots/09b/09b45fba1502e585d35a852f932bd3e2.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 413,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/c2a/c2a7dc4540eb79aaff7099ae691105d3.jpg"
                },
                {
                    "id": 2139724,
                    "image": "https://media.rawg.io/media/screenshots/ccc/ccc8bc96a3863a9a618b01a4df172d8d.jpg"
                },
                {
                    "id": 2139725,
                    "image": "https://media.rawg.io/media/screenshots/c75/c751625ebad334a61c515a5ac7ce4d77.jpg"
                },
                {
                    "id": 2139726,
                    "image": "https://media.rawg.io/media/screenshots/fe1/fe15bb608d9b07692d7c78a6bcb59a2b.jpg"
                },
                {
                    "id": 2708508,
                    "image": "https://media.rawg.io/media/screenshots/f4f/f4f9fadbc1ae5ed2e46bc65f6e7f0333.jpg"
                },
                {
                    "id": 2708509,
                    "image": "https://media.rawg.io/media/screenshots/b21/b212c9c571b50642a8df70efc7031c38.jpg"
                },
                {
                    "id": 2708510,
                    "image": "https://media.rawg.io/media/screenshots/c83/c83fa792db91f6b48df731aa260c64ca.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "shadows-die-twice",
            "name": "Sekiro: Shadows Die Twice",
            "playtime": 14,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2019-03-22",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/67f/67f62d1f062a6164f57575e0604ee9f6.jpg",
            "rating": 4.37,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 1094,
                    "percent": 59.46
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 502,
                    "percent": 27.28
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 160,
                    "percent": 8.7
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 84,
                    "percent": 4.57
                }
            ],
            "ratings_count": 1810,
            "reviews_text_count": 23,
            "added": 6965,
            "added_by_status": {
                "yet": 491,
                "owned": 3299,
                "beaten": 1129,
                "toplay": 1185,
                "dropped": 568,
                "playing": 293
            },
            "metacritic": 90,
            "suggestions_count": 508,
            "updated": "2023-04-15T16:09:30",
            "id": 50734,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 24,
                    "name": "RPG",
                    "slug": "rpg",
                    "language": "eng",
                    "games_count": 17009,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 42412,
                    "name": "Ролевая игра",
                    "slug": "rolevaia-igra",
                    "language": "rus",
                    "games_count": 13302,
                    "image_background": "https://media.rawg.io/media/games/ee3/ee3e10193aafc3230ba1cae426967d10.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42442,
                    "name": "Открытый мир",
                    "slug": "otkrytyi-mir",
                    "language": "rus",
                    "games_count": 4297,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 40845,
                    "name": "Partial Controller Support",
                    "slug": "partial-controller-support",
                    "language": "eng",
                    "games_count": 9594,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42420,
                    "name": "Сложная",
                    "slug": "slozhnaia",
                    "language": "rus",
                    "games_count": 4385,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 42491,
                    "name": "Мясо",
                    "slug": "miaso",
                    "language": "rus",
                    "games_count": 3850,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 49,
                    "name": "Difficult",
                    "slug": "difficult",
                    "language": "eng",
                    "games_count": 13060,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 15,
                    "name": "Stealth",
                    "slug": "stealth",
                    "language": "eng",
                    "games_count": 5846,
                    "image_background": "https://media.rawg.io/media/games/16b/16b1b7b36e2042d1128d5a3e852b3b2f.jpg"
                },
                {
                    "id": 42439,
                    "name": "Стелс",
                    "slug": "stels",
                    "language": "rus",
                    "games_count": 1510,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 97,
                    "name": "Action RPG",
                    "slug": "action-rpg",
                    "language": "eng",
                    "games_count": 5874,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42477,
                    "name": "Мрачная",
                    "slug": "mrachnaia",
                    "language": "rus",
                    "games_count": 3416,
                    "image_background": "https://media.rawg.io/media/games/d9f/d9f982e042df6263684ba1fdea3efc1c.jpg"
                },
                {
                    "id": 42487,
                    "name": "Слэшер",
                    "slug": "slesher",
                    "language": "rus",
                    "games_count": 1862,
                    "image_background": "https://media.rawg.io/media/games/21a/21ad672cedee9b4378abb6c2d2e626ee.jpg"
                },
                {
                    "id": 44,
                    "name": "Nudity",
                    "slug": "nudity",
                    "language": "eng",
                    "games_count": 4792,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 42506,
                    "name": "Тёмное фэнтези",
                    "slug": "tiomnoe-fentezi",
                    "language": "rus",
                    "games_count": 1830,
                    "image_background": "https://media.rawg.io/media/games/cfe/cfe5960b5caca432f3575fc7d8ff736b.jpg"
                },
                {
                    "id": 40,
                    "name": "Dark Fantasy",
                    "slug": "dark-fantasy",
                    "language": "eng",
                    "games_count": 3255,
                    "image_background": "https://media.rawg.io/media/games/501/501e7019925a3c692bf1c8062f07abe6.jpg"
                },
                {
                    "id": 120,
                    "name": "Memes",
                    "slug": "memes",
                    "language": "eng",
                    "games_count": 1573,
                    "image_background": "https://media.rawg.io/media/games/bce/bce62fbc7cf74bf6a1a37340993ec148.jpg"
                },
                {
                    "id": 50,
                    "name": "Sexual Content",
                    "slug": "sexual-content",
                    "language": "eng",
                    "games_count": 4395,
                    "image_background": "https://media.rawg.io/media/games/522/522f66c5f8542a945b9e2b1942f1ad63.jpg"
                },
                {
                    "id": 233,
                    "name": "JRPG",
                    "slug": "jrpg",
                    "language": "eng",
                    "games_count": 3678,
                    "image_background": "https://media.rawg.io/media/screenshots/73e/73e4d78a55248fc26a4e06726b6bd969.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 86,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 278,
                    "name": "Assassin",
                    "slug": "assassin",
                    "language": "eng",
                    "games_count": 733,
                    "image_background": "https://media.rawg.io/media/games/742/74276457ebb9466e11d75a2be7722265.jpg"
                },
                {
                    "id": 42440,
                    "name": "Ассассины",
                    "slug": "assassiny",
                    "language": "rus",
                    "games_count": 252,
                    "image_background": "https://media.rawg.io/media/games/c35/c354856af9151dc63844be4f9843d2c2.jpg"
                },
                {
                    "id": 42592,
                    "name": "Похожа на Dark Souls",
                    "slug": "pokhozha-na-dark-souls",
                    "language": "rus",
                    "games_count": 605,
                    "image_background": "https://media.rawg.io/media/games/718/71891d2484a592d871e91dc826707e1c.jpg"
                },
                {
                    "id": 42584,
                    "name": "Ниндзя",
                    "slug": "nindzia",
                    "language": "rus",
                    "games_count": 362,
                    "image_background": "https://media.rawg.io/media/screenshots/157/1571cdfb52888191eabaf53c2b897240.jpg"
                },
                {
                    "id": 186,
                    "name": "Ninja",
                    "slug": "ninja",
                    "language": "eng",
                    "games_count": 2321,
                    "image_background": "https://media.rawg.io/media/screenshots/033/033f9667f8d25eb544f600429f145b14.jpg"
                },
                {
                    "id": 580,
                    "name": "Souls-like",
                    "slug": "souls-like",
                    "language": "eng",
                    "games_count": 1032,
                    "image_background": "https://media.rawg.io/media/games/043/043f8b4a5d9b767694370d6fbbc8cd3c.jpg"
                },
                {
                    "id": 42618,
                    "name": "Ритм-игра",
                    "slug": "ritm-igra",
                    "language": "rus",
                    "games_count": 725,
                    "image_background": "https://media.rawg.io/media/screenshots/ca9/ca95a5bb74f37b4a483a2e88ec604097.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 1840,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/67f/67f62d1f062a6164f57575e0604ee9f6.jpg"
                },
                {
                    "id": 805136,
                    "image": "https://media.rawg.io/media/screenshots/198/198257c08163153e72a31bd61a6cd70b.jpg"
                },
                {
                    "id": 805137,
                    "image": "https://media.rawg.io/media/screenshots/9b3/9b3add83516f3737b8054c7469be282a.jpg"
                },
                {
                    "id": 805138,
                    "image": "https://media.rawg.io/media/screenshots/64d/64d71a80b0033e091b35c3948046605b.jpg"
                },
                {
                    "id": 805139,
                    "image": "https://media.rawg.io/media/screenshots/8d7/8d77b08c45b3232961b443677fa06a5f.jpg"
                },
                {
                    "id": 805140,
                    "image": "https://media.rawg.io/media/screenshots/a96/a96e960d87fc209488ef25da79b92a84.jpg"
                },
                {
                    "id": 805141,
                    "image": "https://media.rawg.io/media/screenshots/8ed/8edc8d65ba1c1ab001a3fb1bd6fdeeb6.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "beat-saber",
            "name": "Beat Saber",
            "playtime": 6,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2018-05-01",
            "tba": False,
            "background_image": "https://media.rawg.io/media/screenshots/90f/90f61894908915eff8455e7b43d466a2.jpg",
            "rating": 4.37,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 334,
                    "percent": 60.84
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 147,
                    "percent": 26.78
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 37,
                    "percent": 6.74
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 31,
                    "percent": 5.65
                }
            ],
            "ratings_count": 544,
            "reviews_text_count": 4,
            "added": 2077,
            "added_by_status": {
                "yet": 36,
                "owned": 1346,
                "beaten": 185,
                "toplay": 158,
                "dropped": 174,
                "playing": 178
            },
            "metacritic": 90,
            "suggestions_count": 222,
            "updated": "2023-04-16T07:27:19",
            "id": 58325,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 42420,
                    "name": "Сложная",
                    "slug": "slozhnaia",
                    "language": "rus",
                    "games_count": 4385,
                    "image_background": "https://media.rawg.io/media/games/f8c/f8c6a262ead4c16b47e1219310210eb3.jpg"
                },
                {
                    "id": 40850,
                    "name": "Steam Leaderboards",
                    "slug": "steam-leaderboards",
                    "language": "eng",
                    "games_count": 5753,
                    "image_background": "https://media.rawg.io/media/games/59a/59a3ebcba3d08c51532c6ca877aff256.jpg"
                },
                {
                    "id": 42411,
                    "name": "Ранний доступ",
                    "slug": "rannii-dostup",
                    "language": "rus",
                    "games_count": 11500,
                    "image_background": "https://media.rawg.io/media/screenshots/88b/88b5f27f07d6ca2f8a3cd0b36e03a670.jpg"
                },
                {
                    "id": 14,
                    "name": "Early Access",
                    "slug": "early-access",
                    "language": "eng",
                    "games_count": 11980,
                    "image_background": "https://media.rawg.io/media/games/009/009e4e84975d6a60173ec1199db25aa3.jpg"
                },
                {
                    "id": 42407,
                    "name": "Аниме",
                    "slug": "anime-2",
                    "language": "rus",
                    "games_count": 6641,
                    "image_background": "https://media.rawg.io/media/games/a38/a3857b2445c70ac5dbe73b210a827ad8.jpg"
                },
                {
                    "id": 42438,
                    "name": "Поддержка модификаций",
                    "slug": "podderzhka-modifikatsii",
                    "language": "rus",
                    "games_count": 566,
                    "image_background": "https://media.rawg.io/media/games/149/149bbed9d90dc09328ba79bbacfda3c8.jpg"
                },
                {
                    "id": 42612,
                    "name": "Быстрая",
                    "slug": "bystraia",
                    "language": "rus",
                    "games_count": 1499,
                    "image_background": "https://media.rawg.io/media/games/a01/a01b34c722ceec784817381eb1824fa5.jpg"
                },
                {
                    "id": 42561,
                    "name": "Мемы",
                    "slug": "memy",
                    "language": "rus",
                    "games_count": 1387,
                    "image_background": "https://media.rawg.io/media/games/11f/11fd681c312c14644ab360888dba3486.jpg"
                },
                {
                    "id": 33,
                    "name": "VR",
                    "slug": "vr",
                    "language": "eng",
                    "games_count": 11800,
                    "image_background": "https://media.rawg.io/media/screenshots/c02/c02c64324edc2045ea1fc0601cdaaa0c.jpg"
                },
                {
                    "id": 42451,
                    "name": "Будущее",
                    "slug": "budushchee",
                    "language": "rus",
                    "games_count": 2342,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42531,
                    "name": "Спортивная игра",
                    "slug": "sportivnaia-igra",
                    "language": "rus",
                    "games_count": 3435,
                    "image_background": "https://media.rawg.io/media/games/5eb/5eb49eb2fa0738fdb5bacea557b1bc57.jpg"
                },
                {
                    "id": 136,
                    "name": "Music",
                    "slug": "music",
                    "language": "eng",
                    "games_count": 26820,
                    "image_background": "https://media.rawg.io/media/games/f99/f9979698c43fd84c3ab69280576dd3af.jpg"
                },
                {
                    "id": 42620,
                    "name": "Музыка",
                    "slug": "muzyka",
                    "language": "rus",
                    "games_count": 945,
                    "image_background": "https://media.rawg.io/media/screenshots/695/69511e8a8ec8edf9b85c3e68190844a4.jpg"
                },
                {
                    "id": 42507,
                    "name": "Сражения на мечах",
                    "slug": "srazheniia-na-mechakh",
                    "language": "rus",
                    "games_count": 503,
                    "image_background": "https://media.rawg.io/media/screenshots/360/3609a212ee012fad38d06f0cdd616091.jpg"
                },
                {
                    "id": 207,
                    "name": "Rhythm",
                    "slug": "rhythm",
                    "language": "eng",
                    "games_count": 1863,
                    "image_background": "https://media.rawg.io/media/screenshots/90f/90f61894908915eff8455e7b43d466a2.jpg"
                },
                {
                    "id": 42618,
                    "name": "Ритм-игра",
                    "slug": "ritm-igra",
                    "language": "rus",
                    "games_count": 725,
                    "image_background": "https://media.rawg.io/media/screenshots/ca9/ca95a5bb74f37b4a483a2e88ec604097.jpg"
                },
                {
                    "id": 42709,
                    "name": "Звёздные войны",
                    "slug": "zviozdnye-voiny",
                    "language": "rus",
                    "games_count": 53,
                    "image_background": "https://media.rawg.io/media/screenshots/b2d/b2d1dbce92dcbcd5a5d376984c3cb0fe.jpg"
                },
                {
                    "id": 42707,
                    "name": "Генерация на основе музыки",
                    "slug": "generatsiia-na-osnove-muzyki",
                    "language": "rus",
                    "games_count": 172,
                    "image_background": "https://media.rawg.io/media/screenshots/216/21604ad1b0ad028ace5bee1c14e7ee12.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 549,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/screenshots/90f/90f61894908915eff8455e7b43d466a2.jpg"
                },
                {
                    "id": 767729,
                    "image": "https://media.rawg.io/media/screenshots/839/839a84dba406dc444a399431e60e3062.jpg"
                },
                {
                    "id": 767730,
                    "image": "https://media.rawg.io/media/screenshots/9a0/9a02ce2ed44d42fab013389a0bed2e45.jpg"
                },
                {
                    "id": 767731,
                    "image": "https://media.rawg.io/media/screenshots/72f/72f89d777a5578cea3ec89fca5a957f7.jpg"
                },
                {
                    "id": 767732,
                    "image": "https://media.rawg.io/media/screenshots/636/63624af3f929ab0a7332f21e6b1bf2d4.jpg"
                },
                {
                    "id": 767733,
                    "image": "https://media.rawg.io/media/screenshots/90f/90f61894908915eff8455e7b43d466a2.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "doom-eternal",
            "name": "DOOM Eternal",
            "playtime": 12,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2020-03-20",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/3ea/3ea3c9bbd940b6cb7f2139e42d3d443f.jpg",
            "rating": 4.37,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 676,
                    "percent": 56.66
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 358,
                    "percent": 30.01
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 123,
                    "percent": 10.31
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 36,
                    "percent": 3.02
                }
            ],
            "ratings_count": 1164,
            "reviews_text_count": 21,
            "added": 6563,
            "added_by_status": {
                "yet": 469,
                "owned": 3597,
                "beaten": 984,
                "toplay": 1037,
                "dropped": 282,
                "playing": 194
            },
            "metacritic": 86,
            "suggestions_count": 647,
            "updated": "2023-04-14T13:19:32",
            "id": 58777,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 18,
                    "name": "Co-op",
                    "slug": "co-op",
                    "language": "eng",
                    "games_count": 9806,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 42428,
                    "name": "Шутер",
                    "slug": "shuter",
                    "language": "rus",
                    "games_count": 6479,
                    "image_background": "https://media.rawg.io/media/games/c24/c24ec439abf4a2e92f3429dfa83f7f94.jpg"
                },
                {
                    "id": 8,
                    "name": "First-Person",
                    "slug": "first-person",
                    "language": "eng",
                    "games_count": 29966,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 42435,
                    "name": "Шедевр",
                    "slug": "shedevr",
                    "language": "rus",
                    "games_count": 1059,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 32,
                    "name": "Sci-fi",
                    "slug": "sci-fi",
                    "language": "eng",
                    "games_count": 17671,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42423,
                    "name": "Научная фантастика",
                    "slug": "nauchnaia-fantastika",
                    "language": "rus",
                    "games_count": 5796,
                    "image_background": "https://media.rawg.io/media/games/3cf/3cff89996570cf29a10eb9cd967dcf73.jpg"
                },
                {
                    "id": 40845,
                    "name": "Partial Controller Support",
                    "slug": "partial-controller-support",
                    "language": "eng",
                    "games_count": 9594,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 30,
                    "name": "FPS",
                    "slug": "fps",
                    "language": "eng",
                    "games_count": 12754,
                    "image_background": "https://media.rawg.io/media/games/f87/f87457e8347484033cb34cde6101d08d.jpg"
                },
                {
                    "id": 42427,
                    "name": "Шутер от первого лица",
                    "slug": "shuter-ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 3952,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42491,
                    "name": "Мясо",
                    "slug": "miaso",
                    "language": "rus",
                    "games_count": 3850,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 26,
                    "name": "Gore",
                    "slug": "gore",
                    "language": "eng",
                    "games_count": 5083,
                    "image_background": "https://media.rawg.io/media/games/998/9980c4296f311d8bcc5b451ca51e4fe1.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 397,
                    "name": "Online multiplayer",
                    "slug": "online-multiplayer",
                    "language": "eng",
                    "games_count": 3813,
                    "image_background": "https://media.rawg.io/media/games/1bd/1bd2657b81eb0c99338120ad444b24ff.jpg"
                },
                {
                    "id": 42488,
                    "name": "Пост-апокалипсис",
                    "slug": "post-apokalipsis",
                    "language": "rus",
                    "games_count": 750,
                    "image_background": "https://media.rawg.io/media/games/fd2/fd20a68d7ef195855588c937865dd0a7.jpg"
                },
                {
                    "id": 42529,
                    "name": "Для взрослых",
                    "slug": "dlia-vzroslykh",
                    "language": "rus",
                    "games_count": 1877,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 42612,
                    "name": "Быстрая",
                    "slug": "bystraia",
                    "language": "rus",
                    "games_count": 1499,
                    "image_background": "https://media.rawg.io/media/games/a01/a01b34c722ceec784817381eb1824fa5.jpg"
                },
                {
                    "id": 131,
                    "name": "Fast-Paced",
                    "slug": "fast-paced",
                    "language": "eng",
                    "games_count": 10848,
                    "image_background": "https://media.rawg.io/media/games/88a/88af17cc08783ccdd1608ae63c47eeac.jpg"
                },
                {
                    "id": 270,
                    "name": "Blood",
                    "slug": "blood",
                    "language": "eng",
                    "games_count": 1984,
                    "image_background": "https://media.rawg.io/media/games/63f/63f0e68688cad279ed38cde931dbfcdb.jpg"
                },
                {
                    "id": 42577,
                    "name": "Кровь",
                    "slug": "krov",
                    "language": "rus",
                    "games_count": 347,
                    "image_background": "https://media.rawg.io/media/games/e4a/e4ab7f784bdc38c76ce6e4cef9715d18.jpg"
                },
                {
                    "id": 187,
                    "name": "Demons",
                    "slug": "demons",
                    "language": "eng",
                    "games_count": 1950,
                    "image_background": "https://media.rawg.io/media/screenshots/a06/a06ad4fb44d5031dcfa262ffc1759b47.jpg"
                },
                {
                    "id": 42545,
                    "name": "Демоны",
                    "slug": "demony",
                    "language": "rus",
                    "games_count": 1085,
                    "image_background": "https://media.rawg.io/media/games/0b2/0b240149610b8b20eac098b8071f575a.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 1193,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/3ea/3ea3c9bbd940b6cb7f2139e42d3d443f.jpg"
                },
                {
                    "id": 810359,
                    "image": "https://media.rawg.io/media/screenshots/e60/e605ef79d45fcde4afcdbbe8783b7755.jpg"
                },
                {
                    "id": 810360,
                    "image": "https://media.rawg.io/media/screenshots/65d/65db880d23d8d9afe59da1a0f4fbc9d1_s0rkn1r.jpg"
                },
                {
                    "id": 810361,
                    "image": "https://media.rawg.io/media/screenshots/bb4/bb448b8a9aa51ff3e620d3d4c292214b.jpg"
                },
                {
                    "id": 810362,
                    "image": "https://media.rawg.io/media/screenshots/922/922d1b5f0231cf8b0eaa4b78f3935434.jpg"
                },
                {
                    "id": 810363,
                    "image": "https://media.rawg.io/media/screenshots/311/311c4a0364dd23e2ccaabe0fef29f467_U6b7UNM.jpg"
                },
                {
                    "id": 810364,
                    "image": "https://media.rawg.io/media/screenshots/32a/32abc47d857fffc485b86dcd56cbe3c7.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 2,
                    "name": "Shooter",
                    "slug": "shooter"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "psychonauts-2",
            "name": "Psychonauts 2",
            "playtime": 11,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "macOS",
                        "slug": "macos"
                    }
                },
                {
                    "platform": {
                        "id": 6,
                        "name": "Linux",
                        "slug": "linux"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 5,
                        "name": "GOG",
                        "slug": "gog"
                    }
                }
            ],
            "released": "2021-08-24",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/c3c/c3c536cc4d32623ba928020dfd39a648.jpg",
            "rating": 4.36,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 185,
                    "percent": 57.63
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 93,
                    "percent": 28.97
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 29,
                    "percent": 9.03
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 14,
                    "percent": 4.36
                }
            ],
            "ratings_count": 312,
            "reviews_text_count": 8,
            "added": 2423,
            "added_by_status": {
                "yet": 173,
                "owned": 1476,
                "beaten": 243,
                "toplay": 402,
                "dropped": 68,
                "playing": 61
            },
            "metacritic": 88,
            "suggestions_count": 438,
            "updated": "2023-04-15T23:43:45",
            "id": 257192,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 42482,
                    "name": "Смешная",
                    "slug": "smeshnaia",
                    "language": "rus",
                    "games_count": 6256,
                    "image_background": "https://media.rawg.io/media/screenshots/f2f/f2f3c93d6153da7aee590f3ab8ccd803.jpg"
                },
                {
                    "id": 42481,
                    "name": "Юмор",
                    "slug": "iumor",
                    "language": "rus",
                    "games_count": 4048,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a1202a378607b6c635c8f18ace95dd.jpg"
                },
                {
                    "id": 42463,
                    "name": "Платформер",
                    "slug": "platformer-2",
                    "language": "rus",
                    "games_count": 6297,
                    "image_background": "https://media.rawg.io/media/games/89a/89a700d3c6a76bd0610ca89ccd20da54.jpg"
                },
                {
                    "id": 42494,
                    "name": "3D-платформер",
                    "slug": "3d-platformer-2",
                    "language": "rus",
                    "games_count": 2558,
                    "image_background": "https://media.rawg.io/media/games/74d/74dafeb9a442b87b9dd4a1d4a2faa37b.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 321,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/c3c/c3c536cc4d32623ba928020dfd39a648.jpg"
                },
                {
                    "id": 1767973,
                    "image": "https://media.rawg.io/media/screenshots/2d4/2d4130d059e57c6feaa46d011a302200.jpg"
                },
                {
                    "id": 1767974,
                    "image": "https://media.rawg.io/media/screenshots/6dc/6dca1fc477d41d04a34f4f2380b7b543.JPG"
                },
                {
                    "id": 2830387,
                    "image": "https://media.rawg.io/media/screenshots/1b8/1b8dcf75eeb2eac91f51b098c36e28e2.jpg"
                },
                {
                    "id": 2830388,
                    "image": "https://media.rawg.io/media/screenshots/22f/22f8223f6adb979e5b54830118b5f2d8.jpg"
                },
                {
                    "id": 2830389,
                    "image": "https://media.rawg.io/media/screenshots/6fc/6fcdc92a1b21ba550b2cc6c79bc3f1b3.jpg"
                },
                {
                    "id": 2830390,
                    "image": "https://media.rawg.io/media/screenshots/1a8/1a8a37817ebd4a180cb56af6dbe433b2.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 5,
                        "name": "Apple Macintosh",
                        "slug": "mac"
                    }
                },
                {
                    "platform": {
                        "id": 6,
                        "name": "Linux",
                        "slug": "linux"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "astros-playroom",
            "name": "Astro's Playroom",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2020-11-12",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/bfe/bfe7780b7d4342540be2e5273d49e54c.jpg",
            "rating": 4.36,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 226,
                    "percent": 51.02
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 179,
                    "percent": 40.41
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 24,
                    "percent": 5.42
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 14,
                    "percent": 3.16
                }
            ],
            "ratings_count": 438,
            "reviews_text_count": 4,
            "added": 2083,
            "added_by_status": {
                "yet": 37,
                "owned": 1453,
                "beaten": 444,
                "toplay": 48,
                "dropped": 65,
                "playing": 36
            },
            "metacritic": 83,
            "suggestions_count": 142,
            "updated": "2023-04-15T21:53:04",
            "id": 452646,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 37797,
                    "name": "true exclusive",
                    "slug": "true-exclusive",
                    "language": "eng",
                    "games_count": 3995,
                    "image_background": "https://media.rawg.io/media/games/214/214b29aeff13a0ae6a70fc4426e85991.jpg"
                }
            ],
            "esrb_rating": {
                "id": 2,
                "name": "Everyone 10+",
                "slug": "everyone-10-plus",
                "name_en": "Everyone 10+",
                "name_ru": "С 10 лет"
            },
            "user_game": None,
            "reviews_count": 443,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/bfe/bfe7780b7d4342540be2e5273d49e54c.jpg"
                },
                {
                    "id": 2408612,
                    "image": "https://media.rawg.io/media/screenshots/a08/a08e091e1912cfac85c5a48f99a28ccb.jpg"
                },
                {
                    "id": 2408613,
                    "image": "https://media.rawg.io/media/screenshots/300/300771025f192c75a76cdd3ed9229dd9.jpg"
                },
                {
                    "id": 2408614,
                    "image": "https://media.rawg.io/media/screenshots/aed/aed6777a3d7ae19e5411ac5b893e8b33.jpg"
                },
                {
                    "id": 2408616,
                    "image": "https://media.rawg.io/media/screenshots/a98/a98bdb667d28da98e58ca69a9fcdf731.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "ratchet-clank-rift-apart",
            "name": "Ratchet & Clank: Rift Apart",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2021-06-11",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/ccf/ccfd3fd488a8ed61145a3da96c080131.jpg",
            "rating": 4.36,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 120,
                    "percent": 55.3
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 72,
                    "percent": 33.18
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 17,
                    "percent": 7.83
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 8,
                    "percent": 3.69
                }
            ],
            "ratings_count": 209,
            "reviews_text_count": 6,
            "added": 1373,
            "added_by_status": {
                "yet": 81,
                "owned": 702,
                "beaten": 232,
                "toplay": 316,
                "dropped": 14,
                "playing": 28
            },
            "metacritic": 88,
            "suggestions_count": 854,
            "updated": "2023-04-11T10:06:47",
            "id": 727315,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 115,
                    "name": "Controller",
                    "slug": "controller",
                    "language": "eng",
                    "games_count": 9462,
                    "image_background": "https://media.rawg.io/media/games/295/295eb868c241e6ad32ac033b8e6a2ede.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 37797,
                    "name": "true exclusive",
                    "slug": "true-exclusive",
                    "language": "eng",
                    "games_count": 3995,
                    "image_background": "https://media.rawg.io/media/games/214/214b29aeff13a0ae6a70fc4426e85991.jpg"
                },
                {
                    "id": 5816,
                    "name": "console",
                    "slug": "console",
                    "language": "eng",
                    "games_count": 1412,
                    "image_background": "https://media.rawg.io/media/games/faa/faa6a4a7a2e57faf2960329630aee211.jpg"
                },
                {
                    "id": 4565,
                    "name": "offline",
                    "slug": "offline",
                    "language": "eng",
                    "games_count": 1086,
                    "image_background": "https://media.rawg.io/media/games/4fe/4feffcec6315c5f5a96442a8444431ca.jpg"
                },
                {
                    "id": 2326,
                    "name": "explore",
                    "slug": "explore",
                    "language": "eng",
                    "games_count": 3298,
                    "image_background": "https://media.rawg.io/media/games/cd2/cd2a1a360839002bceadc5a8b3c7dbf7.jpg"
                },
                {
                    "id": 1709,
                    "name": "work",
                    "slug": "work",
                    "language": "eng",
                    "games_count": 9597,
                    "image_background": "https://media.rawg.io/media/games/6e3/6e319b00ea9844539b3b20753d8ca0b4.jpg"
                },
                {
                    "id": 1105,
                    "name": "planet",
                    "slug": "planet",
                    "language": "eng",
                    "games_count": 3116,
                    "image_background": "https://media.rawg.io/media/games/187/18725d2559e75fdfbe019333682c0ec8.jpg"
                },
                {
                    "id": 2405,
                    "name": "planets",
                    "slug": "planets",
                    "language": "eng",
                    "games_count": 1535,
                    "image_background": "https://media.rawg.io/media/screenshots/2da/2daaa79a4108669455cf7a234afe7905.jpeg"
                },
                {
                    "id": 3758,
                    "name": "speed",
                    "slug": "speed",
                    "language": "eng",
                    "games_count": 8205,
                    "image_background": "https://media.rawg.io/media/screenshots/0f8/0f8f34410d8f86a5c528a421b2429485.jpg"
                },
                {
                    "id": 5033,
                    "name": "tv",
                    "slug": "tv",
                    "language": "eng",
                    "games_count": 562,
                    "image_background": "https://media.rawg.io/media/screenshots/a53/a53a888ccfb190e3c743f45d5bdba0a3.jpg"
                }
            ],
            "esrb_rating": {
                "id": 2,
                "name": "Everyone 10+",
                "slug": "everyone-10-plus",
                "name_en": "Everyone 10+",
                "name_ru": "С 10 лет"
            },
            "user_game": None,
            "reviews_count": 217,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/ccf/ccfd3fd488a8ed61145a3da96c080131.jpg"
                },
                {
                    "id": 2778288,
                    "image": "https://media.rawg.io/media/screenshots/6bf/6bf00977809c0b2ae9fd9bb86bd0a0bb.jpg"
                },
                {
                    "id": 2778289,
                    "image": "https://media.rawg.io/media/screenshots/8c3/8c3ea9ea331f0dc85d1f3b9007eb9f06.jpg"
                },
                {
                    "id": 2778290,
                    "image": "https://media.rawg.io/media/screenshots/2d0/2d08c4275d6c6d4fc8110b0c454c9a76.jpg"
                },
                {
                    "id": 2778291,
                    "image": "https://media.rawg.io/media/screenshots/88c/88ce64c4f1d8677ac62e2a5916eca9ac.jpg"
                },
                {
                    "id": 2778292,
                    "image": "https://media.rawg.io/media/screenshots/de5/de52eb1a0a4256293de1db609b52feb6.jpg"
                },
                {
                    "id": 2778293,
                    "image": "https://media.rawg.io/media/screenshots/d3e/d3e93a61a5a15cc367672efffacee760.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "final-fantasy-vii-remake-intergrade",
            "name": "FINAL FANTASY VII REMAKE INTERGRADE",
            "playtime": 4,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 11,
                        "name": "Epic Games",
                        "slug": "epic-games"
                    }
                }
            ],
            "released": "2021-06-10",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/acf/acf26d699ac392c014656f7fb3224d3d.jpg",
            "rating": 4.35,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 21,
                    "percent": 52.5
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 14,
                    "percent": 35.0
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 4,
                    "percent": 10.0
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 1,
                    "percent": 2.5
                }
            ],
            "ratings_count": 38,
            "reviews_text_count": 2,
            "added": 337,
            "added_by_status": {
                "yet": 31,
                "owned": 212,
                "beaten": 44,
                "toplay": 42,
                "dropped": 3,
                "playing": 5
            },
            "metacritic": 88,
            "suggestions_count": 246,
            "updated": "2023-04-13T08:22:26",
            "id": 586199,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 24,
                    "name": "RPG",
                    "slug": "rpg",
                    "language": "eng",
                    "games_count": 17009,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 42412,
                    "name": "Ролевая игра",
                    "slug": "rolevaia-igra",
                    "language": "rus",
                    "games_count": 13302,
                    "image_background": "https://media.rawg.io/media/games/ee3/ee3e10193aafc3230ba1cae426967d10.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 32,
                    "name": "Sci-fi",
                    "slug": "sci-fi",
                    "language": "eng",
                    "games_count": 17671,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42423,
                    "name": "Научная фантастика",
                    "slug": "nauchnaia-fantastika",
                    "language": "rus",
                    "games_count": 5796,
                    "image_background": "https://media.rawg.io/media/games/3cf/3cff89996570cf29a10eb9cd967dcf73.jpg"
                },
                {
                    "id": 42480,
                    "name": "Фэнтези",
                    "slug": "fentezi",
                    "language": "rus",
                    "games_count": 7813,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 64,
                    "name": "Fantasy",
                    "slug": "fantasy",
                    "language": "eng",
                    "games_count": 25175,
                    "image_background": "https://media.rawg.io/media/games/33d/33df5a032898b8ab7e3773c7a5f1d336.jpg"
                },
                {
                    "id": 42416,
                    "name": "Контроллер",
                    "slug": "kontroller",
                    "language": "rus",
                    "games_count": 3643,
                    "image_background": "https://media.rawg.io/media/games/e04/e04963f3ac4c4fa83a1dc0b9231e50db.jpg"
                },
                {
                    "id": 97,
                    "name": "Action RPG",
                    "slug": "action-rpg",
                    "language": "eng",
                    "games_count": 5874,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 42489,
                    "name": "Ролевой экшен",
                    "slug": "rolevoi-ekshen",
                    "language": "rus",
                    "games_count": 2557,
                    "image_background": "https://media.rawg.io/media/games/5be/5bec14622f6faf804a592176577c1347.jpg"
                },
                {
                    "id": 115,
                    "name": "Controller",
                    "slug": "controller",
                    "language": "eng",
                    "games_count": 9462,
                    "image_background": "https://media.rawg.io/media/games/295/295eb868c241e6ad32ac033b8e6a2ede.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42490,
                    "name": "Приключенческий экшен",
                    "slug": "prikliuchencheskii-ekshen",
                    "language": "rus",
                    "games_count": 5545,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 42460,
                    "name": "Реализм",
                    "slug": "realizm",
                    "language": "rus",
                    "games_count": 3621,
                    "image_background": "https://media.rawg.io/media/games/bff/bff7d82316cddea9541261a045ba008a.jpg"
                },
                {
                    "id": 110,
                    "name": "Cinematic",
                    "slug": "cinematic",
                    "language": "eng",
                    "games_count": 1313,
                    "image_background": "https://media.rawg.io/media/games/7ac/7aca7ccf0e70cd0974cb899ab9e5158e.jpg"
                },
                {
                    "id": 77,
                    "name": "Realistic",
                    "slug": "realistic",
                    "language": "eng",
                    "games_count": 3658,
                    "image_background": "https://media.rawg.io/media/games/106/1069e754e7e6012b0cf42b4b04704792.jpg"
                },
                {
                    "id": 39,
                    "name": "Building",
                    "slug": "building",
                    "language": "eng",
                    "games_count": 5115,
                    "image_background": "https://media.rawg.io/media/games/bda/bdab2603c0dc67268d0610449bc7df16.jpg"
                },
                {
                    "id": 82,
                    "name": "Magic",
                    "slug": "magic",
                    "language": "eng",
                    "games_count": 8201,
                    "image_background": "https://media.rawg.io/media/games/417/4176298c1b22ccd338ce3dfc34eb7e28.jpg"
                },
                {
                    "id": 42478,
                    "name": "Магия",
                    "slug": "magiia",
                    "language": "rus",
                    "games_count": 2599,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 571,
                    "name": "3D",
                    "slug": "3d",
                    "language": "eng",
                    "games_count": 81983,
                    "image_background": "https://media.rawg.io/media/screenshots/066/066eb1b7a3f332b8089645fbf8c3ebdc.jpg"
                },
                {
                    "id": 406,
                    "name": "Story",
                    "slug": "story",
                    "language": "eng",
                    "games_count": 11617,
                    "image_background": "https://media.rawg.io/media/games/2ee/2eeed8524931b4fae1e4a40d0e5443b5.jpg"
                },
                {
                    "id": 42623,
                    "name": "Кинематографичная",
                    "slug": "kinematografichnaia",
                    "language": "rus",
                    "games_count": 1219,
                    "image_background": "https://media.rawg.io/media/games/708/7080e6c87e0825cb02888bf3c44b3889.jpg"
                },
                {
                    "id": 271,
                    "name": "Remake",
                    "slug": "remake",
                    "language": "eng",
                    "games_count": 1767,
                    "image_background": "https://media.rawg.io/media/games/7a4/7a45e4cdc5b07f316d49cf147b083b27.jpg"
                },
                {
                    "id": 233,
                    "name": "JRPG",
                    "slug": "jrpg",
                    "language": "eng",
                    "games_count": 3678,
                    "image_background": "https://media.rawg.io/media/screenshots/73e/73e4d78a55248fc26a4e06726b6bd969.jpg"
                },
                {
                    "id": 40937,
                    "name": "Steam Trading Cards",
                    "slug": "steam-trading-cards-2",
                    "language": "eng",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 42514,
                    "name": "Японская ролевая игра",
                    "slug": "iaponskaia-rolevaia-igra",
                    "language": "rus",
                    "games_count": 1823,
                    "image_background": "https://media.rawg.io/media/games/0d4/0d4e5446db732e2fcce34d1dcb4dd914.jpg"
                },
                {
                    "id": 42494,
                    "name": "3D-платформер",
                    "slug": "3d-platformer-2",
                    "language": "rus",
                    "games_count": 2558,
                    "image_background": "https://media.rawg.io/media/games/74d/74dafeb9a442b87b9dd4a1d4a2faa37b.jpg"
                },
                {
                    "id": 209,
                    "name": "Drama",
                    "slug": "drama",
                    "language": "eng",
                    "games_count": 2671,
                    "image_background": "https://media.rawg.io/media/games/b0a/b0a370527fea0e824225269d4a8797db.jpg"
                },
                {
                    "id": 229,
                    "name": "3D Platformer",
                    "slug": "3d-platformer",
                    "language": "eng",
                    "games_count": 8988,
                    "image_background": "https://media.rawg.io/media/screenshots/57f/57f97397220442e71c51f9ba44b67fec_KzipzFC.jpeg"
                },
                {
                    "id": 42650,
                    "name": "Драма",
                    "slug": "drama-2",
                    "language": "rus",
                    "games_count": 2034,
                    "image_background": "https://media.rawg.io/media/games/f0a/f0a65d7d9c4534f8f4897f9d161307ed.jpg"
                },
                {
                    "id": 5816,
                    "name": "console",
                    "slug": "console",
                    "language": "eng",
                    "games_count": 1412,
                    "image_background": "https://media.rawg.io/media/games/faa/faa6a4a7a2e57faf2960329630aee211.jpg"
                },
                {
                    "id": 42625,
                    "name": "Партийная ролевая игра",
                    "slug": "partiinaia-rolevaia-igra",
                    "language": "rus",
                    "games_count": 738,
                    "image_background": "https://media.rawg.io/media/games/424/424facd40f4eb1f2794fe4b4bb28a277.jpg"
                },
                {
                    "id": 206,
                    "name": "Party-Based RPG",
                    "slug": "party-based-rpg",
                    "language": "eng",
                    "games_count": 685,
                    "image_background": "https://media.rawg.io/media/games/a9c/a9c789951de65da545d51f664b4f2ce0.jpg"
                },
                {
                    "id": 4565,
                    "name": "offline",
                    "slug": "offline",
                    "language": "eng",
                    "games_count": 1086,
                    "image_background": "https://media.rawg.io/media/games/4fe/4feffcec6315c5f5a96442a8444431ca.jpg"
                },
                {
                    "id": 42493,
                    "name": "Зрелищные сражения",
                    "slug": "zrelishchnye-srazheniia",
                    "language": "rus",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/8d4/8d46786ca86b1d95f3dc7e700e2dc4dd.jpg"
                },
                {
                    "id": 254,
                    "name": "Spectacle fighter",
                    "slug": "spectacle-fighter",
                    "language": "eng",
                    "games_count": 386,
                    "image_background": "https://media.rawg.io/media/games/566/566f53f43aa1bd28c63cf3a4d21440ee.jpg"
                },
                {
                    "id": 822,
                    "name": "escape",
                    "slug": "escape",
                    "language": "eng",
                    "games_count": 7888,
                    "image_background": "https://media.rawg.io/media/screenshots/474/47478ccb205e4e0d0117986107625599.jpg"
                },
                {
                    "id": 5641,
                    "name": "bundle",
                    "slug": "bundle",
                    "language": "eng",
                    "games_count": 432,
                    "image_background": "https://media.rawg.io/media/screenshots/c93/c93b6722c7dcf1ac6d237c1fd3ae3847.jpg"
                },
                {
                    "id": 311,
                    "name": "Underground",
                    "slug": "underground",
                    "language": "eng",
                    "games_count": 433,
                    "image_background": "https://media.rawg.io/media/screenshots/fee/feebf7913e3e7dcda406e19fbee8bedc.jpg"
                },
                {
                    "id": 6706,
                    "name": "connect",
                    "slug": "connect",
                    "language": "eng",
                    "games_count": 463,
                    "image_background": "https://media.rawg.io/media/screenshots/3fc/3fcbb5f9ce1d88f3a0bf315fa06ab16b.jpg"
                },
                {
                    "id": 64540,
                    "name": "Подземная",
                    "slug": "podzemnaia",
                    "language": "rus",
                    "games_count": 203,
                    "image_background": "https://media.rawg.io/media/screenshots/72e/72ee87a21101a37c2c838a14ebe3c859.jpg"
                },
                {
                    "id": 5479,
                    "name": "drive",
                    "slug": "drive",
                    "language": "eng",
                    "games_count": 944,
                    "image_background": "https://media.rawg.io/media/screenshots/b3d/b3df40065f51627e1f7fdc70135317c7_DHhrVjl.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 40,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/acf/acf26d699ac392c014656f7fb3224d3d.jpg"
                },
                {
                    "id": 2796965,
                    "image": "https://media.rawg.io/media/screenshots/5a0/5a08e2ebbdaa6b1b1a1f1858a80922f9.jpg"
                },
                {
                    "id": 2796966,
                    "image": "https://media.rawg.io/media/screenshots/691/6912544b0b3d3d25e7cca3ab54ae4d7e.jpg"
                },
                {
                    "id": 2796967,
                    "image": "https://media.rawg.io/media/screenshots/609/60962852f2a5f11ed325af3ff2c8e881.jpg"
                },
                {
                    "id": 2796968,
                    "image": "https://media.rawg.io/media/screenshots/993/9934a06277fa5ce4578dbe9bd587c388.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "super-mario-3d-world-bowsers-fury",
            "name": "Super Mario 3D World + Bowser’s Fury",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 6,
                        "name": "Nintendo Store",
                        "slug": "nintendo"
                    }
                }
            ],
            "released": "2021-02-12",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/cd2/cd22f0dcf8f080086c60f77eed7a8a93.jpg",
            "rating": 4.35,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 108,
                    "percent": 53.47
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 72,
                    "percent": 35.64
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 14,
                    "percent": 6.93
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 8,
                    "percent": 3.96
                }
            ],
            "ratings_count": 198,
            "reviews_text_count": 3,
            "added": 588,
            "added_by_status": {
                "yet": 54,
                "owned": 90,
                "beaten": 178,
                "toplay": 159,
                "dropped": 39,
                "playing": 68
            },
            "metacritic": 89,
            "suggestions_count": 339,
            "updated": "2023-04-08T23:47:05",
            "id": 487916,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 72,
                    "name": "Local Multiplayer",
                    "slug": "local-multiplayer",
                    "language": "eng",
                    "games_count": 12874,
                    "image_background": "https://media.rawg.io/media/games/aa3/aa36ba4b486a03ddfaef274fb4f5afd4.jpg"
                },
                {
                    "id": 480,
                    "name": "Platform",
                    "slug": "platform",
                    "language": "eng",
                    "games_count": 315,
                    "image_background": "https://media.rawg.io/media/screenshots/9c3/9c3ebd9ec57d7dc4dae0756bbede3d26.jpg"
                }
            ],
            "esrb_rating": {
                "id": 1,
                "name": "Everyone",
                "slug": "everyone",
                "name_en": "Everyone",
                "name_ru": "Для всех"
            },
            "user_game": None,
            "reviews_count": 202,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/cd2/cd22f0dcf8f080086c60f77eed7a8a93.jpg"
                },
                {
                    "id": 2505836,
                    "image": "https://media.rawg.io/media/screenshots/c8d/c8dc57300ea8c7c1c7b88b0a20ed1119.jpg"
                },
                {
                    "id": 2505837,
                    "image": "https://media.rawg.io/media/screenshots/e48/e48e2ed455d8c2ae952f14be783d10bf.jpg"
                },
                {
                    "id": 2505838,
                    "image": "https://media.rawg.io/media/screenshots/78a/78a66d5490bb9bc8d3c0e1cf64e5dd16.jpg"
                },
                {
                    "id": 2505839,
                    "image": "https://media.rawg.io/media/screenshots/b04/b044dbdf21b74db12b39e4d70f61d84a.jpg"
                },
                {
                    "id": 2505840,
                    "image": "https://media.rawg.io/media/screenshots/47c/47c889a3d82a5e3f2c6cc19e71eb58bb.jpg"
                },
                {
                    "id": 2505841,
                    "image": "https://media.rawg.io/media/screenshots/ed4/ed483a07ec51bb4b8120a6b988713e8d.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 83,
                    "name": "Platformer",
                    "slug": "platformer"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "black-mesa",
            "name": "Black Mesa",
            "playtime": 6,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 6,
                        "name": "Linux",
                        "slug": "linux"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                }
            ],
            "released": "2020-03-06",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/009/009e4e84975d6a60173ec1199db25aa3.jpg",
            "rating": 4.34,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 468,
                    "percent": 50.92
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 356,
                    "percent": 38.74
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 66,
                    "percent": 7.18
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 29,
                    "percent": 3.16
                }
            ],
            "ratings_count": 909,
            "reviews_text_count": 5,
            "added": 5016,
            "added_by_status": {
                "yet": 374,
                "owned": 3320,
                "beaten": 709,
                "toplay": 335,
                "dropped": 195,
                "playing": 83
            },
            "metacritic": 86,
            "suggestions_count": 503,
            "updated": "2023-04-10T13:03:03",
            "id": 15426,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 18,
                    "name": "Co-op",
                    "slug": "co-op",
                    "language": "eng",
                    "games_count": 9806,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42428,
                    "name": "Шутер",
                    "slug": "shuter",
                    "language": "rus",
                    "games_count": 6479,
                    "image_background": "https://media.rawg.io/media/games/c24/c24ec439abf4a2e92f3429dfa83f7f94.jpg"
                },
                {
                    "id": 8,
                    "name": "First-Person",
                    "slug": "first-person",
                    "language": "eng",
                    "games_count": 29966,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 32,
                    "name": "Sci-fi",
                    "slug": "sci-fi",
                    "language": "eng",
                    "games_count": 17671,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42423,
                    "name": "Научная фантастика",
                    "slug": "nauchnaia-fantastika",
                    "language": "rus",
                    "games_count": 5796,
                    "image_background": "https://media.rawg.io/media/games/3cf/3cff89996570cf29a10eb9cd967dcf73.jpg"
                },
                {
                    "id": 40845,
                    "name": "Partial Controller Support",
                    "slug": "partial-controller-support",
                    "language": "eng",
                    "games_count": 9594,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 30,
                    "name": "FPS",
                    "slug": "fps",
                    "language": "eng",
                    "games_count": 12754,
                    "image_background": "https://media.rawg.io/media/games/f87/f87457e8347484033cb34cde6101d08d.jpg"
                },
                {
                    "id": 42427,
                    "name": "Шутер от первого лица",
                    "slug": "shuter-ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 3952,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42461,
                    "name": "Классика",
                    "slug": "klassika",
                    "language": "rus",
                    "games_count": 1391,
                    "image_background": "https://media.rawg.io/media/games/bc0/bc06a29ceac58652b684deefe7d56099.jpg"
                },
                {
                    "id": 193,
                    "name": "Classic",
                    "slug": "classic",
                    "language": "eng",
                    "games_count": 1767,
                    "image_background": "https://media.rawg.io/media/games/14a/14a83c56ff668baaced6e8c8704b6391.jpg"
                },
                {
                    "id": 397,
                    "name": "Online multiplayer",
                    "slug": "online-multiplayer",
                    "language": "eng",
                    "games_count": 3813,
                    "image_background": "https://media.rawg.io/media/games/1bd/1bd2657b81eb0c99338120ad444b24ff.jpg"
                },
                {
                    "id": 42411,
                    "name": "Ранний доступ",
                    "slug": "rannii-dostup",
                    "language": "rus",
                    "games_count": 11500,
                    "image_background": "https://media.rawg.io/media/screenshots/88b/88b5f27f07d6ca2f8a3cd0b36e03a670.jpg"
                },
                {
                    "id": 14,
                    "name": "Early Access",
                    "slug": "early-access",
                    "language": "eng",
                    "games_count": 11980,
                    "image_background": "https://media.rawg.io/media/games/009/009e4e84975d6a60173ec1199db25aa3.jpg"
                },
                {
                    "id": 63,
                    "name": "Zombies",
                    "slug": "zombies",
                    "language": "eng",
                    "games_count": 10130,
                    "image_background": "https://media.rawg.io/media/games/d64/d646810b629081cc12aec49ed9f49441.jpg"
                },
                {
                    "id": 40838,
                    "name": "Includes level editor",
                    "slug": "includes-level-editor",
                    "language": "eng",
                    "games_count": 1613,
                    "image_background": "https://media.rawg.io/media/games/054/0549f1a0a5e782d4e81cdf8d022073fa.jpg"
                },
                {
                    "id": 40832,
                    "name": "Cross-Platform Multiplayer",
                    "slug": "cross-platform-multiplayer",
                    "language": "eng",
                    "games_count": 2188,
                    "image_background": "https://media.rawg.io/media/screenshots/4f4/4f4722571e32954af43a4508607c1748.jpg"
                },
                {
                    "id": 42544,
                    "name": "Зомби",
                    "slug": "zombi-2",
                    "language": "rus",
                    "games_count": 1929,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 40833,
                    "name": "Captions available",
                    "slug": "captions-available",
                    "language": "eng",
                    "games_count": 1221,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 172,
                    "name": "Aliens",
                    "slug": "aliens",
                    "language": "eng",
                    "games_count": 6441,
                    "image_background": "https://media.rawg.io/media/games/34b/34b1f1850a1c06fd971bc6ab3ac0ce0e.jpg"
                },
                {
                    "id": 42485,
                    "name": "Инопланетяне",
                    "slug": "inoplanetiane",
                    "language": "rus",
                    "games_count": 1258,
                    "image_background": "https://media.rawg.io/media/games/c24/c24f4434882ae9c2c8d9d38de82cb7a5.jpg"
                },
                {
                    "id": 37797,
                    "name": "true exclusive",
                    "slug": "true-exclusive",
                    "language": "eng",
                    "games_count": 3995,
                    "image_background": "https://media.rawg.io/media/games/214/214b29aeff13a0ae6a70fc4426e85991.jpg"
                },
                {
                    "id": 42466,
                    "name": "Римейк",
                    "slug": "rimeik",
                    "language": "rus",
                    "games_count": 206,
                    "image_background": "https://media.rawg.io/media/games/8fc/8fc59e74133fd8a8a436b7e2d0fb36c2.jpg"
                },
                {
                    "id": 271,
                    "name": "Remake",
                    "slug": "remake",
                    "language": "eng",
                    "games_count": 1767,
                    "image_background": "https://media.rawg.io/media/games/7a4/7a45e4cdc5b07f316d49cf147b083b27.jpg"
                },
                {
                    "id": 40839,
                    "name": "Includes Source SDK",
                    "slug": "includes-source-sdk",
                    "language": "eng",
                    "games_count": 60,
                    "image_background": "https://media.rawg.io/media/games/48e/48e63bbddeddbe9ba81942772b156664.jpg"
                },
                {
                    "id": 244,
                    "name": "Mod",
                    "slug": "mod",
                    "language": "eng",
                    "games_count": 1777,
                    "image_background": "https://media.rawg.io/media/screenshots/a2e/a2ecf055ac9339d3a58808842c44a9b7.jpg"
                },
                {
                    "id": 42557,
                    "name": "Модификации",
                    "slug": "modifikatsii",
                    "language": "rus",
                    "games_count": 63,
                    "image_background": "https://media.rawg.io/media/screenshots/5ff/5ff7e855a4d0f4de1bfa515cd0e19071.jpg"
                }
            ],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 919,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/009/009e4e84975d6a60173ec1199db25aa3.jpg"
                },
                {
                    "id": 136136,
                    "image": "https://media.rawg.io/media/screenshots/2d4/2d42ff888b242347b68e6aafcb01d407.jpg"
                },
                {
                    "id": 136137,
                    "image": "https://media.rawg.io/media/screenshots/43c/43c62529e311d38cd3a59a4840c9989a.jpg"
                },
                {
                    "id": 136138,
                    "image": "https://media.rawg.io/media/screenshots/0ab/0abfdd7c1859d049478ef78595cba277.jpg"
                },
                {
                    "id": 136139,
                    "image": "https://media.rawg.io/media/screenshots/d20/d209a1ae9b43a5d723793cde762d3962.jpg"
                },
                {
                    "id": 136140,
                    "image": "https://media.rawg.io/media/screenshots/621/621ac4a8b944755f9cfe0decd30fe248.jpg"
                },
                {
                    "id": 136141,
                    "image": "https://media.rawg.io/media/screenshots/e62/e62b354bd970dfc297c9172556526803.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 6,
                        "name": "Linux",
                        "slug": "linux"
                    }
                }
            ],
            "genres": [
                {
                    "id": 2,
                    "name": "Shooter",
                    "slug": "shooter"
                },
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "signalis",
            "name": "Signalis",
            "playtime": 3,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo Switch",
                        "slug": "nintendo-switch"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                }
            ],
            "released": "2022-10-27",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/480/480295ba922318bb052d169174ec88aa.jpg",
            "rating": 4.34,
            "rating_top": 4,
            "ratings": [
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 39,
                    "percent": 45.35
                },
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 38,
                    "percent": 44.19
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 9,
                    "percent": 10.47
                }
            ],
            "ratings_count": 83,
            "reviews_text_count": 1,
            "added": 712,
            "added_by_status": {
                "yet": 39,
                "owned": 434,
                "beaten": 73,
                "toplay": 119,
                "dropped": 25,
                "playing": 22
            },
            "metacritic": 82,
            "suggestions_count": 307,
            "updated": "2023-04-16T16:19:11",
            "id": 424978,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 45113,
                    "image_background": "https://media.rawg.io/media/games/8cc/8cce7c0e99dcc43d66c8efd42f9d03e3.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 32,
                    "name": "Sci-fi",
                    "slug": "sci-fi",
                    "language": "eng",
                    "games_count": 17671,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42423,
                    "name": "Научная фантастика",
                    "slug": "nauchnaia-fantastika",
                    "language": "rus",
                    "games_count": 5796,
                    "image_background": "https://media.rawg.io/media/games/3cf/3cff89996570cf29a10eb9cd967dcf73.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 189,
                    "name": "Female Protagonist",
                    "slug": "female-protagonist",
                    "language": "eng",
                    "games_count": 10677,
                    "image_background": "https://media.rawg.io/media/games/1fb/1fb1c5f7a71d771f440b27ce7f71e7eb.jpg"
                },
                {
                    "id": 42404,
                    "name": "Женщина-протагонист",
                    "slug": "zhenshchina-protagonist",
                    "language": "rus",
                    "games_count": 2416,
                    "image_background": "https://media.rawg.io/media/games/7f6/7f6cd70ba2ad57053b4847c13569f2d8.jpg"
                },
                {
                    "id": 42402,
                    "name": "Насилие",
                    "slug": "nasilie",
                    "language": "rus",
                    "games_count": 4763,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 34,
                    "name": "Violent",
                    "slug": "violent",
                    "language": "eng",
                    "games_count": 5908,
                    "image_background": "https://media.rawg.io/media/games/152/152e788b7504aa2753c86dae912fb34c.jpg"
                },
                {
                    "id": 42415,
                    "name": "Пиксельная графика",
                    "slug": "pikselnaia-grafika",
                    "language": "rus",
                    "games_count": 8585,
                    "image_background": "https://media.rawg.io/media/games/bbf/bbf8d74ab64440ad76294cff2f4d9cfa.jpg"
                },
                {
                    "id": 42467,
                    "name": "Ретро",
                    "slug": "retro-2",
                    "language": "rus",
                    "games_count": 5520,
                    "image_background": "https://media.rawg.io/media/games/9fa/9fa63622543e5d4f6d99aa9d73b043de.jpg"
                },
                {
                    "id": 122,
                    "name": "Pixel Graphics",
                    "slug": "pixel-graphics",
                    "language": "eng",
                    "games_count": 95727,
                    "image_background": "https://media.rawg.io/media/screenshots/d68/d684c5ec81b8ea46bfd4b5c3bae4007f.jpg"
                },
                {
                    "id": 74,
                    "name": "Retro",
                    "slug": "retro",
                    "language": "eng",
                    "games_count": 41775,
                    "image_background": "https://media.rawg.io/media/screenshots/6fe/6fe228662a253cd929cc78a103541ee0.jpg"
                },
                {
                    "id": 134,
                    "name": "Anime",
                    "slug": "anime",
                    "language": "eng",
                    "games_count": 11173,
                    "image_background": "https://media.rawg.io/media/games/cc5/cc576aa274780702ef93463f5410031e.jpg"
                },
                {
                    "id": 42407,
                    "name": "Аниме",
                    "slug": "anime-2",
                    "language": "rus",
                    "games_count": 6641,
                    "image_background": "https://media.rawg.io/media/games/a38/a3857b2445c70ac5dbe73b210a827ad8.jpg"
                },
                {
                    "id": 42471,
                    "name": "Хоррор на выживание",
                    "slug": "khorror-na-vyzhivanie",
                    "language": "rus",
                    "games_count": 2127,
                    "image_background": "https://media.rawg.io/media/games/447/4470c1e76f01acfaf5af9c207d1c1c92.jpg"
                },
                {
                    "id": 17,
                    "name": "Survival Horror",
                    "slug": "survival-horror",
                    "language": "eng",
                    "games_count": 8163,
                    "image_background": "https://media.rawg.io/media/games/b54/b54598d1d5cc31899f4f0a7e3122a7b0.jpg"
                },
                {
                    "id": 42556,
                    "name": "Тайна",
                    "slug": "taina",
                    "language": "rus",
                    "games_count": 3559,
                    "image_background": "https://media.rawg.io/media/games/948/948fe7f00b6cba8472f5ecd07a455077.jpg"
                },
                {
                    "id": 117,
                    "name": "Mystery",
                    "slug": "mystery",
                    "language": "eng",
                    "games_count": 12105,
                    "image_background": "https://media.rawg.io/media/screenshots/9d2/9d22689a1c2a7ced9d1690e0c5c66871.jpg"
                }
            ],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 86,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/480/480295ba922318bb052d169174ec88aa.jpg"
                },
                {
                    "id": 2327057,
                    "image": "https://media.rawg.io/media/screenshots/1ba/1ba77befb152970f5b21546aa1aef370.jpg"
                },
                {
                    "id": 2327058,
                    "image": "https://media.rawg.io/media/screenshots/dde/dde918a415dc05de5335f707723e6f08.jpg"
                },
                {
                    "id": 2327059,
                    "image": "https://media.rawg.io/media/screenshots/11f/11f517b83221d481fac6f98cf3366677.jpg"
                },
                {
                    "id": 2327061,
                    "image": "https://media.rawg.io/media/screenshots/298/29887c49ca3032ad6c21c43ff7e875e0.jpg"
                },
                {
                    "id": 2327062,
                    "image": "https://media.rawg.io/media/screenshots/0a3/0a337262e0cc880a5222cafa9128c6bd.jpg"
                },
                {
                    "id": 2327063,
                    "image": "https://media.rawg.io/media/screenshots/81d/81d38f9d4f011debb22d25d4b8497960.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 7,
                        "name": "Nintendo",
                        "slug": "nintendo"
                    }
                }
            ],
            "genres": [
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "death-stranding",
            "name": "Death Stranding",
            "playtime": 9,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 11,
                        "name": "Epic Games",
                        "slug": "epic-games"
                    }
                }
            ],
            "released": "2019-11-08",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/2ad/2ad87a4a69b1104f02435c14c5196095.jpg",
            "rating": 4.34,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 1070,
                    "percent": 58.15
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 487,
                    "percent": 26.47
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 198,
                    "percent": 10.76
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 85,
                    "percent": 4.62
                }
            ],
            "ratings_count": 1791,
            "reviews_text_count": 31,
            "added": 8235,
            "added_by_status": {
                "yet": 639,
                "owned": 4233,
                "beaten": 1315,
                "toplay": 1355,
                "dropped": 350,
                "playing": 343
            },
            "metacritic": 84,
            "suggestions_count": 539,
            "updated": "2023-04-13T14:10:51",
            "id": 50738,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 42400,
                    "name": "Атмосфера",
                    "slug": "atmosfera",
                    "language": "rus",
                    "games_count": 6103,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4457,
                    "image_background": "https://media.rawg.io/media/games/fc1/fc1307a2774506b5bd65d7e8424664a7.jpg"
                },
                {
                    "id": 42,
                    "name": "Great Soundtrack",
                    "slug": "great-soundtrack",
                    "language": "eng",
                    "games_count": 3233,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42394,
                    "name": "Глубокий сюжет",
                    "slug": "glubokii-siuzhet",
                    "language": "rus",
                    "games_count": 8617,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 118,
                    "name": "Story Rich",
                    "slug": "story-rich",
                    "language": "eng",
                    "games_count": 18495,
                    "image_background": "https://media.rawg.io/media/games/960/960b601d9541cec776c5fa42a00bf6c4.jpg"
                },
                {
                    "id": 42442,
                    "name": "Открытый мир",
                    "slug": "otkrytyi-mir",
                    "language": "rus",
                    "games_count": 4297,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 42435,
                    "name": "Шедевр",
                    "slug": "shedevr",
                    "language": "rus",
                    "games_count": 1059,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 32,
                    "name": "Sci-fi",
                    "slug": "sci-fi",
                    "language": "eng",
                    "games_count": 17671,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42423,
                    "name": "Научная фантастика",
                    "slug": "nauchnaia-fantastika",
                    "language": "rus",
                    "games_count": 5796,
                    "image_background": "https://media.rawg.io/media/games/3cf/3cff89996570cf29a10eb9cd967dcf73.jpg"
                },
                {
                    "id": 40845,
                    "name": "Partial Controller Support",
                    "slug": "partial-controller-support",
                    "language": "eng",
                    "games_count": 9594,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 16,
                    "name": "Horror",
                    "slug": "horror",
                    "language": "eng",
                    "games_count": 45056,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 1,
                    "name": "Survival",
                    "slug": "survival",
                    "language": "eng",
                    "games_count": 7130,
                    "image_background": "https://media.rawg.io/media/games/d7d/d7d33daa1892e2468cd0263d5dfc957e.jpg"
                },
                {
                    "id": 42452,
                    "name": "Выживание",
                    "slug": "vyzhivanie",
                    "language": "rus",
                    "games_count": 4550,
                    "image_background": "https://media.rawg.io/media/games/daa/daaee07fcb40744d90cf8142f94a241f.jpg"
                },
                {
                    "id": 42464,
                    "name": "Исследование",
                    "slug": "issledovanie",
                    "language": "rus",
                    "games_count": 2990,
                    "image_background": "https://media.rawg.io/media/screenshots/8f0/8f0b94922ad5e59968852649697b2643.jpg"
                },
                {
                    "id": 15,
                    "name": "Stealth",
                    "slug": "stealth",
                    "language": "eng",
                    "games_count": 5846,
                    "image_background": "https://media.rawg.io/media/games/16b/16b1b7b36e2042d1128d5a3e852b3b2f.jpg"
                },
                {
                    "id": 42439,
                    "name": "Стелс",
                    "slug": "stels",
                    "language": "rus",
                    "games_count": 1510,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 42406,
                    "name": "Нагота",
                    "slug": "nagota",
                    "language": "rus",
                    "games_count": 4399,
                    "image_background": "https://media.rawg.io/media/games/a0e/a0ef08621301a1eab5e04fa5c96978fa.jpeg"
                },
                {
                    "id": 44,
                    "name": "Nudity",
                    "slug": "nudity",
                    "language": "eng",
                    "games_count": 4792,
                    "image_background": "https://media.rawg.io/media/games/618/618c2031a07bbff6b4f611f10b6bcdbc.jpg"
                },
                {
                    "id": 43,
                    "name": "Post-apocalyptic",
                    "slug": "post-apocalyptic",
                    "language": "eng",
                    "games_count": 3351,
                    "image_background": "https://media.rawg.io/media/games/8d6/8d69eb6c32ed6acfd75f82d532144993.jpg"
                },
                {
                    "id": 42488,
                    "name": "Пост-апокалипсис",
                    "slug": "post-apokalipsis",
                    "language": "rus",
                    "games_count": 750,
                    "image_background": "https://media.rawg.io/media/games/fd2/fd20a68d7ef195855588c937865dd0a7.jpg"
                },
                {
                    "id": 110,
                    "name": "Cinematic",
                    "slug": "cinematic",
                    "language": "eng",
                    "games_count": 1313,
                    "image_background": "https://media.rawg.io/media/games/7ac/7aca7ccf0e70cd0974cb899ab9e5158e.jpg"
                },
                {
                    "id": 42555,
                    "name": "Симулятор ходьбы",
                    "slug": "simuliator-khodby",
                    "language": "rus",
                    "games_count": 1717,
                    "image_background": "https://media.rawg.io/media/screenshots/8f0/8f0b94922ad5e59968852649697b2643.jpg"
                },
                {
                    "id": 120,
                    "name": "Memes",
                    "slug": "memes",
                    "language": "eng",
                    "games_count": 1573,
                    "image_background": "https://media.rawg.io/media/games/bce/bce62fbc7cf74bf6a1a37340993ec148.jpg"
                },
                {
                    "id": 172,
                    "name": "Aliens",
                    "slug": "aliens",
                    "language": "eng",
                    "games_count": 6441,
                    "image_background": "https://media.rawg.io/media/games/34b/34b1f1850a1c06fd971bc6ab3ac0ce0e.jpg"
                },
                {
                    "id": 91,
                    "name": "Walking Simulator",
                    "slug": "walking-simulator",
                    "language": "eng",
                    "games_count": 6427,
                    "image_background": "https://media.rawg.io/media/games/948/948fe7f00b6cba8472f5ecd07a455077.jpg"
                },
                {
                    "id": 42623,
                    "name": "Кинематографичная",
                    "slug": "kinematografichnaia",
                    "language": "rus",
                    "games_count": 1219,
                    "image_background": "https://media.rawg.io/media/games/708/7080e6c87e0825cb02888bf3c44b3889.jpg"
                },
                {
                    "id": 478,
                    "name": "3rd-Person Perspective",
                    "slug": "3rd-person-perspective",
                    "language": "eng",
                    "games_count": 86,
                    "image_background": "https://media.rawg.io/media/games/de6/de66bc4c72b45c3bb906c85d0628112d.jpg"
                },
                {
                    "id": 209,
                    "name": "Drama",
                    "slug": "drama",
                    "language": "eng",
                    "games_count": 2671,
                    "image_background": "https://media.rawg.io/media/games/b0a/b0a370527fea0e824225269d4a8797db.jpg"
                },
                {
                    "id": 216,
                    "name": "Heist",
                    "slug": "heist",
                    "language": "eng",
                    "games_count": 455,
                    "image_background": "https://media.rawg.io/media/games/59a/59a3ebcba3d08c51532c6ca877aff256.jpg"
                },
                {
                    "id": 42447,
                    "name": "Ограбления",
                    "slug": "ogrableniia",
                    "language": "rus",
                    "games_count": 178,
                    "image_background": "https://media.rawg.io/media/games/5a9/5a9e785af72ae88026380f7987f23d90.jpg"
                },
                {
                    "id": 578,
                    "name": "Masterpiece",
                    "slug": "masterpiece",
                    "language": "eng",
                    "games_count": 276,
                    "image_background": "https://media.rawg.io/media/games/0fa/0fa9e2b8397b332902d3b56c73888d52.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 1840,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/2ad/2ad87a4a69b1104f02435c14c5196095.jpg"
                },
                {
                    "id": 802887,
                    "image": "https://media.rawg.io/media/screenshots/9da/9da640f5aa62f6fc00a4d1d255460737.jpg"
                },
                {
                    "id": 802890,
                    "image": "https://media.rawg.io/media/screenshots/3d2/3d2a4337cf7673b086a1623d9e5ed2f3.jpg"
                },
                {
                    "id": 802891,
                    "image": "https://media.rawg.io/media/screenshots/5f3/5f3bc8289f9545db69a30fc414e94186.jpg"
                },
                {
                    "id": 802894,
                    "image": "https://media.rawg.io/media/screenshots/2b7/2b731c32ebc308c30abe974cd1266648.jpg"
                },
                {
                    "id": 802895,
                    "image": "https://media.rawg.io/media/screenshots/460/4606e5ba14266eb2292cea7444e4239b.jpg"
                },
                {
                    "id": 802896,
                    "image": "https://media.rawg.io/media/screenshots/2f1/2f10403f41e636dac29d1af2c5c1b982.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "synth-riders",
            "name": "Synth Riders",
            "playtime": 1,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                }
            ],
            "released": "2018-07-12",
            "tba": False,
            "background_image": "https://media.rawg.io/media/screenshots/1af/1af606e2a8f72509574e68bc6d64a3ef.jpg",
            "rating": 4.33,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 3,
                    "percent": 50.0
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 2,
                    "percent": 33.33
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 1,
                    "percent": 16.67
                }
            ],
            "ratings_count": 6,
            "reviews_text_count": 0,
            "added": 186,
            "added_by_status": {
                "yet": 3,
                "owned": 174,
                "beaten": 1,
                "toplay": 1,
                "dropped": 2,
                "playing": 5
            },
            "metacritic": 86,
            "suggestions_count": 169,
            "updated": "2023-02-25T07:56:07",
            "id": 60894,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 211657,
                    "image_background": "https://media.rawg.io/media/games/120/1201a40e4364557b124392ee50317b99.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 32576,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31106,
                    "image_background": "https://media.rawg.io/media/games/46d/46d98e6910fbc0706e2948a7cc9b10c5.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29599,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 42398,
                    "name": "Инди",
                    "slug": "indi-2",
                    "language": "rus",
                    "games_count": 44855,
                    "image_background": "https://media.rawg.io/media/games/f99/f9979698c43fd84c3ab69280576dd3af.jpg"
                },
                {
                    "id": 42401,
                    "name": "Отличный саундтрек",
                    "slug": "otlichnyi-saundtrek",
                    "language": "rus",
                    "games_count": 4454,
                    "image_background": "https://media.rawg.io/media/games/ee3/ee3e10193aafc3230ba1cae426967d10.jpg"
                },
                {
                    "id": 42399,
                    "name": "Казуальная игра",
                    "slug": "kazualnaia-igra",
                    "language": "rus",
                    "games_count": 30399,
                    "image_background": "https://media.rawg.io/media/games/0fd/0fd84d36596a83ef2e5a35f63a072218.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7159,
                    "image_background": "https://media.rawg.io/media/games/d58/d588947d4286e7b5e0e12e1bea7d9844.jpg"
                },
                {
                    "id": 42420,
                    "name": "Сложная",
                    "slug": "slozhnaia",
                    "language": "rus",
                    "games_count": 4365,
                    "image_background": "https://media.rawg.io/media/games/806/8060a7663364ac23e15480728938d6f3.jpg"
                },
                {
                    "id": 40850,
                    "name": "Steam Leaderboards",
                    "slug": "steam-leaderboards",
                    "language": "eng",
                    "games_count": 5723,
                    "image_background": "https://media.rawg.io/media/games/476/476178ef18ab0534771d099f51cdc694.jpg"
                },
                {
                    "id": 42467,
                    "name": "Ретро",
                    "slug": "retro-2",
                    "language": "rus",
                    "games_count": 5449,
                    "image_background": "https://media.rawg.io/media/games/226/2262cea0b385db6cf399f4be831603b0.jpg"
                },
                {
                    "id": 42411,
                    "name": "Ранний доступ",
                    "slug": "rannii-dostup",
                    "language": "rus",
                    "games_count": 11380,
                    "image_background": "https://media.rawg.io/media/games/87a/87a29bcc56b6b6082ead1dd5e2510aaa.jpg"
                },
                {
                    "id": 14,
                    "name": "Early Access",
                    "slug": "early-access",
                    "language": "eng",
                    "games_count": 11860,
                    "image_background": "https://media.rawg.io/media/games/adb/adb59be81367b19c2544457424bcf086.jpg"
                },
                {
                    "id": 42612,
                    "name": "Быстрая",
                    "slug": "bystraia",
                    "language": "rus",
                    "games_count": 1493,
                    "image_background": "https://media.rawg.io/media/screenshots/12e/12ee2600684863837596c0dbb1923fca.jpg"
                },
                {
                    "id": 33,
                    "name": "VR",
                    "slug": "vr",
                    "language": "eng",
                    "games_count": 11749,
                    "image_background": "https://media.rawg.io/media/games/739/73990e3ec9f43a9e8ecafe207fa4f368.jpg"
                },
                {
                    "id": 42531,
                    "name": "Спортивная игра",
                    "slug": "sportivnaia-igra",
                    "language": "rus",
                    "games_count": 3408,
                    "image_background": "https://media.rawg.io/media/games/27b/27b02ffaab6b250cc31bf43baca1fc34.jpg"
                },
                {
                    "id": 42620,
                    "name": "Музыка",
                    "slug": "muzyka",
                    "language": "rus",
                    "games_count": 941,
                    "image_background": "https://media.rawg.io/media/screenshots/de7/de72fd1c417d394d726d4b004f57c36e.jpg"
                },
                {
                    "id": 42618,
                    "name": "Ритм-игра",
                    "slug": "ritm-igra",
                    "language": "rus",
                    "games_count": 718,
                    "image_background": "https://media.rawg.io/media/screenshots/560/560f7bd45d2f8ce3deb42c97fd1d1f49.jpg"
                }
            ],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 6,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/screenshots/1af/1af606e2a8f72509574e68bc6d64a3ef.jpg"
                },
                {
                    "id": 833959,
                    "image": "https://media.rawg.io/media/screenshots/f79/f790a04b8027c7123e0f39856150d742.jpg"
                },
                {
                    "id": 833960,
                    "image": "https://media.rawg.io/media/screenshots/189/189181488d5e4e2f8b14272b96803b99.jpg"
                },
                {
                    "id": 833961,
                    "image": "https://media.rawg.io/media/screenshots/07d/07d01a5df8fcfe5bc865001a145c8d5c.jpg"
                },
                {
                    "id": 833962,
                    "image": "https://media.rawg.io/media/screenshots/91b/91b0abed4c25fe9be386e5bb8768450c.jpg"
                },
                {
                    "id": 833963,
                    "image": "https://media.rawg.io/media/screenshots/754/7547cf5e6d0bc25f26e059d633ed7a63.jpg"
                },
                {
                    "id": 833964,
                    "image": "https://media.rawg.io/media/screenshots/1af/1af606e2a8f72509574e68bc6d64a3ef.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 40,
                    "name": "Casual",
                    "slug": "casual"
                },
                {
                    "id": 51,
                    "name": "Indie",
                    "slug": "indie"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        },
        {
            "slug": "yakuza-7",
            "name": "Yakuza: Like a Dragon",
            "playtime": 17,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 187,
                        "name": "PlayStation 5",
                        "slug": "playstation5"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                }
            ],
            "released": "2020-01-16",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/a59/a5993b9f84944570a31cb6ad08bfe502.jpg",
            "rating": 4.33,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 157,
                    "percent": 60.38
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 65,
                    "percent": 25.0
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 21,
                    "percent": 8.08
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 17,
                    "percent": 6.54
                }
            ],
            "ratings_count": 248,
            "reviews_text_count": 8,
            "added": 2123,
            "added_by_status": {
                "yet": 184,
                "owned": 1273,
                "beaten": 168,
                "toplay": 355,
                "dropped": 72,
                "playing": 71
            },
            "metacritic": 85,
            "suggestions_count": 659,
            "updated": "2023-04-11T07:55:12",
            "id": 369157,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 24,
                    "name": "RPG",
                    "slug": "rpg",
                    "language": "eng",
                    "games_count": 17009,
                    "image_background": "https://media.rawg.io/media/games/d1a/d1a2e99ade53494c6330a0ed945fe823.jpg"
                },
                {
                    "id": 1465,
                    "name": "combat",
                    "slug": "combat",
                    "language": "eng",
                    "games_count": 9132,
                    "image_background": "https://media.rawg.io/media/games/0a5/0a56e2bb9ce95359e69ff9689c553a45.jpg"
                },
                {
                    "id": 144,
                    "name": "Crime",
                    "slug": "crime",
                    "language": "eng",
                    "games_count": 2580,
                    "image_background": "https://media.rawg.io/media/games/9e5/9e5b274c7e3aa5e30beba31b834b0e7e.jpg"
                },
                {
                    "id": 2030,
                    "name": "city",
                    "slug": "city",
                    "language": "eng",
                    "games_count": 9269,
                    "image_background": "https://media.rawg.io/media/games/4fb/4fb548e4816c84d1d70f1a228fb167cc.jpg"
                },
                {
                    "id": 5816,
                    "name": "console",
                    "slug": "console",
                    "language": "eng",
                    "games_count": 1412,
                    "image_background": "https://media.rawg.io/media/games/faa/faa6a4a7a2e57faf2960329630aee211.jpg"
                },
                {
                    "id": 625,
                    "name": "party",
                    "slug": "party",
                    "language": "eng",
                    "games_count": 4052,
                    "image_background": "https://media.rawg.io/media/games/278/27873379c6d27b968babbeefa9b44da3.jpg"
                },
                {
                    "id": 4565,
                    "name": "offline",
                    "slug": "offline",
                    "language": "eng",
                    "games_count": 1086,
                    "image_background": "https://media.rawg.io/media/games/4fe/4feffcec6315c5f5a96442a8444431ca.jpg"
                },
                {
                    "id": 1309,
                    "name": "hero",
                    "slug": "hero",
                    "language": "eng",
                    "games_count": 4847,
                    "image_background": "https://media.rawg.io/media/games/d56/d564ee964eb3c17892b3b35dd607f836.jpg"
                },
                {
                    "id": 1407,
                    "name": "race",
                    "slug": "race",
                    "language": "eng",
                    "games_count": 6826,
                    "image_background": "https://media.rawg.io/media/games/2ec/2ec8d2b5d990b9407e20dc81d271300d.jpg"
                },
                {
                    "id": 2232,
                    "name": "journey",
                    "slug": "journey",
                    "language": "eng",
                    "games_count": 1920,
                    "image_background": "https://media.rawg.io/media/screenshots/387/3873e4dad2efab0da657e6df50739f5f.jpg"
                },
                {
                    "id": 8234,
                    "name": "fall",
                    "slug": "fall",
                    "language": "eng",
                    "games_count": 3608,
                    "image_background": "https://media.rawg.io/media/screenshots/1ae/1aef4421d7f96e4fb8bb8d121cd3e703_SS9Fznj.jpg"
                },
                {
                    "id": 650,
                    "name": "prison",
                    "slug": "prison",
                    "language": "eng",
                    "games_count": 829,
                    "image_background": "https://media.rawg.io/media/screenshots/a32/a32cc76652a0f6c74c5437f9a678638d.jpg"
                },
                {
                    "id": 576,
                    "name": "Faith",
                    "slug": "faith",
                    "language": "eng",
                    "games_count": 322,
                    "image_background": "https://media.rawg.io/media/screenshots/4a4/4a42502b3420a6edb928ec9ed6e66d80.jpg"
                },
                {
                    "id": 815,
                    "name": "sega",
                    "slug": "sega",
                    "language": "eng",
                    "games_count": 143,
                    "image_background": "https://media.rawg.io/media/screenshots/0a2/0a2b3c1d0639057e0945d76ec9710fea.jpg"
                }
            ],
            "esrb_rating": {
                "id": 4,
                "name": "Mature",
                "slug": "mature",
                "name_en": "Mature",
                "name_ru": "С 17 лет"
            },
            "user_game": None,
            "reviews_count": 260,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/a59/a5993b9f84944570a31cb6ad08bfe502.jpg"
                },
                {
                    "id": 2740225,
                    "image": "https://media.rawg.io/media/screenshots/fe4/fe46eb2e5202596fecd6e49d2f2e2a2d.jpg"
                },
                {
                    "id": 2740226,
                    "image": "https://media.rawg.io/media/screenshots/a38/a383a81329e83ab3596cb9d1e2eb291d.jpg"
                },
                {
                    "id": 2740227,
                    "image": "https://media.rawg.io/media/screenshots/366/36624960d4a696926592df7a0000e9b1.jpg"
                },
                {
                    "id": 2740228,
                    "image": "https://media.rawg.io/media/screenshots/7b5/7b550763ba14cdc887507c3af4399a1c.jpg"
                },
                {
                    "id": 2740229,
                    "image": "https://media.rawg.io/media/screenshots/d90/d9062d07216196afce4a53f369dc6dfe.jpg"
                },
                {
                    "id": 2740230,
                    "image": "https://media.rawg.io/media/screenshots/67a/67a2832e930a6348218872d7c04a6308.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                }
            ],
            "genres": [
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 5,
                    "name": "RPG",
                    "slug": "role-playing-games-rpg"
                }
            ]
        },
        {
            "slug": "forza-horizon-5",
            "name": "Forza Horizon 5",
            "playtime": 13,
            "platforms": [
                {
                    "platform": {
                        "id": 4,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 1,
                        "name": "Xbox One",
                        "slug": "xbox-one"
                    }
                },
                {
                    "platform": {
                        "id": 186,
                        "name": "Xbox Series S/X",
                        "slug": "xbox-series-x"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "iOS",
                        "slug": "ios"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 1,
                        "name": "Steam",
                        "slug": "steam"
                    }
                },
                {
                    "store": {
                        "id": 2,
                        "name": "Xbox Store",
                        "slug": "xbox-store"
                    }
                },
                {
                    "store": {
                        "id": 4,
                        "name": "App Store",
                        "slug": "apple-appstore"
                    }
                }
            ],
            "released": "2021-11-08",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/082/082365507ff04d456c700157072d35db.jpg",
            "rating": 4.33,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 270,
                    "percent": 48.47
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 225,
                    "percent": 40.39
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 50,
                    "percent": 8.98
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 12,
                    "percent": 2.15
                }
            ],
            "ratings_count": 544,
            "reviews_text_count": 9,
            "added": 3956,
            "added_by_status": {
                "yet": 124,
                "owned": 2876,
                "beaten": 201,
                "toplay": 281,
                "dropped": 245,
                "playing": 229
            },
            "metacritic": 92,
            "suggestions_count": 514,
            "updated": "2023-04-16T20:10:41",
            "id": 622492,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 42396,
                    "name": "Для одного игрока",
                    "slug": "dlia-odnogo-igroka",
                    "language": "rus",
                    "games_count": 33036,
                    "image_background": "https://media.rawg.io/media/games/511/5118aff5091cb3efec399c808f8c598f.jpg"
                },
                {
                    "id": 42417,
                    "name": "Экшен",
                    "slug": "ekshen",
                    "language": "rus",
                    "games_count": 31341,
                    "image_background": "https://media.rawg.io/media/games/b8c/b8c243eaa0fbac8115e0cdccac3f91dc.jpg"
                },
                {
                    "id": 42392,
                    "name": "Приключение",
                    "slug": "prikliuchenie",
                    "language": "rus",
                    "games_count": 29286,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 40847,
                    "name": "Steam Achievements",
                    "slug": "steam-achievements",
                    "language": "eng",
                    "games_count": 29808,
                    "image_background": "https://media.rawg.io/media/games/310/3106b0e012271c5ffb16497b070be739.jpg"
                },
                {
                    "id": 7,
                    "name": "Multiplayer",
                    "slug": "multiplayer",
                    "language": "eng",
                    "games_count": 36011,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 40836,
                    "name": "Full controller support",
                    "slug": "full-controller-support",
                    "language": "eng",
                    "games_count": 13993,
                    "image_background": "https://media.rawg.io/media/games/4be/4be6a6ad0364751a96229c56bf69be59.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 40849,
                    "name": "Steam Cloud",
                    "slug": "steam-cloud",
                    "language": "eng",
                    "games_count": 13772,
                    "image_background": "https://media.rawg.io/media/games/4cf/4cfc6b7f1850590a4634b08bfab308ab.jpg"
                },
                {
                    "id": 42425,
                    "name": "Для нескольких игроков",
                    "slug": "dlia-neskolkikh-igrokov",
                    "language": "rus",
                    "games_count": 7601,
                    "image_background": "https://media.rawg.io/media/games/6fc/6fcf4cd3b17c288821388e6085bb0fc9.jpg"
                },
                {
                    "id": 18,
                    "name": "Co-op",
                    "slug": "co-op",
                    "language": "eng",
                    "games_count": 9806,
                    "image_background": "https://media.rawg.io/media/games/15c/15c95a4915f88a3e89c821526afe05fc.jpg"
                },
                {
                    "id": 42442,
                    "name": "Открытый мир",
                    "slug": "otkrytyi-mir",
                    "language": "rus",
                    "games_count": 4297,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 411,
                    "name": "cooperative",
                    "slug": "cooperative",
                    "language": "eng",
                    "games_count": 3973,
                    "image_background": "https://media.rawg.io/media/games/baf/baf9905270314e07e6850cffdb51df41.jpg"
                },
                {
                    "id": 8,
                    "name": "First-Person",
                    "slug": "first-person",
                    "language": "eng",
                    "games_count": 29966,
                    "image_background": "https://media.rawg.io/media/games/26d/26d4437715bee60138dab4a7c8c59c92.jpg"
                },
                {
                    "id": 42429,
                    "name": "От первого лица",
                    "slug": "ot-pervogo-litsa",
                    "language": "rus",
                    "games_count": 7260,
                    "image_background": "https://media.rawg.io/media/games/9dd/9ddabb34840ea9227556670606cf8ea3.jpg"
                },
                {
                    "id": 149,
                    "name": "Third Person",
                    "slug": "third-person",
                    "language": "eng",
                    "games_count": 9506,
                    "image_background": "https://media.rawg.io/media/games/d82/d82990b9c67ba0d2d09d4e6fa88885a7.jpg"
                },
                {
                    "id": 42441,
                    "name": "От третьего лица",
                    "slug": "ot-tretego-litsa",
                    "language": "rus",
                    "games_count": 4680,
                    "image_background": "https://media.rawg.io/media/games/da1/da1b267764d77221f07a4386b6548e5a.jpg"
                },
                {
                    "id": 42413,
                    "name": "Симулятор",
                    "slug": "simuliator",
                    "language": "rus",
                    "games_count": 14645,
                    "image_background": "https://media.rawg.io/media/games/0bd/0bd5646a3d8ee0ac3314bced91ea306d.jpg"
                },
                {
                    "id": 9,
                    "name": "Online Co-Op",
                    "slug": "online-co-op",
                    "language": "eng",
                    "games_count": 4246,
                    "image_background": "https://media.rawg.io/media/games/d69/d69810315bd7e226ea2d21f9156af629.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 42587,
                    "name": "Аркада",
                    "slug": "arkada",
                    "language": "rus",
                    "games_count": 7255,
                    "image_background": "https://media.rawg.io/media/games/a32/a32c9c299488ca99afc3fcea605a7718.jpg"
                },
                {
                    "id": 40832,
                    "name": "Cross-Platform Multiplayer",
                    "slug": "cross-platform-multiplayer",
                    "language": "eng",
                    "games_count": 2188,
                    "image_background": "https://media.rawg.io/media/screenshots/4f4/4f4722571e32954af43a4508607c1748.jpg"
                },
                {
                    "id": 157,
                    "name": "PvP",
                    "slug": "pvp",
                    "language": "eng",
                    "games_count": 7102,
                    "image_background": "https://media.rawg.io/media/games/9c4/9c47f320eb73c9a02d462e12f6206b26.jpg"
                },
                {
                    "id": 42434,
                    "name": "Игрок против игрока",
                    "slug": "igrok-protiv-igroka",
                    "language": "rus",
                    "games_count": 3392,
                    "image_background": "https://media.rawg.io/media/games/9af/9af24c1886e2c7b52a4a2c65aa874638.jpg"
                },
                {
                    "id": 42460,
                    "name": "Реализм",
                    "slug": "realizm",
                    "language": "rus",
                    "games_count": 3621,
                    "image_background": "https://media.rawg.io/media/games/bff/bff7d82316cddea9541261a045ba008a.jpg"
                },
                {
                    "id": 42496,
                    "name": "Гонки",
                    "slug": "gonki",
                    "language": "rus",
                    "games_count": 2839,
                    "image_background": "https://media.rawg.io/media/games/8f3/8f306808c45a4dbe0cd698e0b142af08.jpg"
                },
                {
                    "id": 42531,
                    "name": "Спортивная игра",
                    "slug": "sportivnaia-igra",
                    "language": "rus",
                    "games_count": 3435,
                    "image_background": "https://media.rawg.io/media/games/5eb/5eb49eb2fa0738fdb5bacea557b1bc57.jpg"
                },
                {
                    "id": 42690,
                    "name": "Красивая",
                    "slug": "krasivaia",
                    "language": "rus",
                    "games_count": 537,
                    "image_background": "https://media.rawg.io/media/games/90c/90caf1fcb836cad70013452f6f239008.jpg"
                },
                {
                    "id": 45878,
                    "name": "Online PvP",
                    "slug": "online-pvp",
                    "language": "eng",
                    "games_count": 3021,
                    "image_background": "https://media.rawg.io/media/games/c3b/c3be1d5f55cb9324c97ccb7aaaf42ad4.jpg"
                },
                {
                    "id": 40937,
                    "name": "Steam Trading Cards",
                    "slug": "steam-trading-cards-2",
                    "language": "eng",
                    "games_count": 394,
                    "image_background": "https://media.rawg.io/media/games/569/56978b5a77f13aa2ec5d09ec81d01cad.jpg"
                },
                {
                    "id": 130,
                    "name": "Driving",
                    "slug": "driving",
                    "language": "eng",
                    "games_count": 4767,
                    "image_background": "https://media.rawg.io/media/games/5fa/5fae5fec3c943179e09da67a4427d68f.jpg"
                },
                {
                    "id": 42600,
                    "name": "Вождение",
                    "slug": "vozhdenie",
                    "language": "rus",
                    "games_count": 1094,
                    "image_background": "https://media.rawg.io/media/games/7a6/7a6f90e85a2e264c3b440bb4787cf378.jpg"
                },
                {
                    "id": 58132,
                    "name": "Атмосферная",
                    "slug": "atmosfernaia",
                    "language": "rus",
                    "games_count": 4619,
                    "image_background": "https://media.rawg.io/media/games/044/044b2ee023930ca138deda151f40c18c.jpg"
                },
                {
                    "id": 577,
                    "name": "Beautiful",
                    "slug": "beautiful",
                    "language": "eng",
                    "games_count": 1820,
                    "image_background": "https://media.rawg.io/media/games/d3e/d3ee2d7653cf9d4640335ff7a471ab07.jpg"
                },
                {
                    "id": 66533,
                    "name": "Исследования",
                    "slug": "issledovaniia",
                    "language": "rus",
                    "games_count": 4241,
                    "image_background": "https://media.rawg.io/media/games/bde/bdef96f7782fba0ff62dabc37ff4b1f0.jpg"
                },
                {
                    "id": 70351,
                    "name": "Сетевой кооператив",
                    "slug": "setevoi-kooperativ",
                    "language": "rus",
                    "games_count": 810,
                    "image_background": "https://media.rawg.io/media/screenshots/6ab/6abb5456a795b7713919db7568a2fd96.jpg"
                },
                {
                    "id": 1632,
                    "name": "cars",
                    "slug": "cars",
                    "language": "eng",
                    "games_count": 5889,
                    "image_background": "https://media.rawg.io/media/screenshots/bb0/bb0d4cdd201f2bc5ef45ea7897613b68.jpg"
                },
                {
                    "id": 58142,
                    "name": "Автосимулятор",
                    "slug": "avtosimuliator",
                    "language": "rus",
                    "games_count": 453,
                    "image_background": "https://media.rawg.io/media/screenshots/2f1/2f1696be27b8deed7e6283bab12af839.jpg"
                },
                {
                    "id": 2156,
                    "name": "drift",
                    "slug": "drift",
                    "language": "eng",
                    "games_count": 1416,
                    "image_background": "https://media.rawg.io/media/screenshots/d30/d30482d99a7d8fcc58502beb03e93014.jpg"
                },
                {
                    "id": 5270,
                    "name": "festival",
                    "slug": "festival",
                    "language": "eng",
                    "games_count": 27,
                    "image_background": "https://media.rawg.io/media/screenshots/905/905a23335d6f58cbf259309a07877fc8.jpg"
                },
                {
                    "id": 9336,
                    "name": "mexico",
                    "slug": "mexico",
                    "language": "eng",
                    "games_count": 85,
                    "image_background": "https://media.rawg.io/media/screenshots/e3a/e3a982d04a8242d840c8f0f6c4dea963.jpg"
                },
                {
                    "id": 8803,
                    "name": "racing-game",
                    "slug": "racing-game",
                    "language": "eng",
                    "games_count": 41,
                    "image_background": "https://media.rawg.io/media/games/0d2/0d2d58673f3ffc125daa0e9eb61a66c1.jpg"
                },
                {
                    "id": 12669,
                    "name": "sprint",
                    "slug": "sprint",
                    "language": "eng",
                    "games_count": 8,
                    "image_background": "https://media.rawg.io/media/screenshots/3c7/3c7b94767997dc2a29296106c634c53b.jpg"
                },
                {
                    "id": 27142,
                    "name": "photorealism",
                    "slug": "photorealism",
                    "language": "eng",
                    "games_count": 2,
                    "image_background": "https://media.rawg.io/media/screenshots/fb6/fb6bf0655098fbd2f4e6473569f660fb.jpg"
                }
            ],
            "esrb_rating": None,
            "user_game": None,
            "reviews_count": 557,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/082/082365507ff04d456c700157072d35db.jpg"
                },
                {
                    "id": 2882904,
                    "image": "https://media.rawg.io/media/screenshots/5e2/5e2e7ccb084034da25d0b21b7c03c273.jpg"
                },
                {
                    "id": 2882905,
                    "image": "https://media.rawg.io/media/screenshots/6c6/6c69fe99ec23d08b2b0a62feb9d89c65.jpg"
                },
                {
                    "id": 2882906,
                    "image": "https://media.rawg.io/media/screenshots/32c/32c5651c381e6b628c5ac681601a036a.jpg"
                },
                {
                    "id": 2882907,
                    "image": "https://media.rawg.io/media/screenshots/312/3122a56932654c304a60e9ef762277a7.jpg"
                },
                {
                    "id": 2882908,
                    "image": "https://media.rawg.io/media/screenshots/04c/04c7be71d5fd1abace38c90aaa95529d.jpg"
                },
                {
                    "id": 2882909,
                    "image": "https://media.rawg.io/media/screenshots/797/7979f94d39181787ee248a423191563f.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 1,
                        "name": "PC",
                        "slug": "pc"
                    }
                },
                {
                    "platform": {
                        "id": 3,
                        "name": "Xbox",
                        "slug": "xbox"
                    }
                },
                {
                    "platform": {
                        "id": 4,
                        "name": "iOS",
                        "slug": "ios"
                    }
                }
            ],
            "genres": [
                {
                    "id": 1,
                    "name": "Racing",
                    "slug": "racing"
                },
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "id": 14,
                    "name": "Simulation",
                    "slug": "simulation"
                },
                {
                    "id": 15,
                    "name": "Sports",
                    "slug": "sports"
                }
            ]
        },
        {
            "slug": "shadow-of-the-colossus-2018",
            "name": "Shadow of the Colossus  (2018)",
            "playtime": 0,
            "platforms": [
                {
                    "platform": {
                        "id": 18,
                        "name": "PlayStation 4",
                        "slug": "playstation4"
                    }
                }
            ],
            "stores": [
                {
                    "store": {
                        "id": 3,
                        "name": "PlayStation Store",
                        "slug": "playstation-store"
                    }
                }
            ],
            "released": "2018-02-06",
            "tba": False,
            "background_image": "https://media.rawg.io/media/games/5c5/5c5089af36b99bf9465357a8556449f9.jpg",
            "rating": 4.32,
            "rating_top": 5,
            "ratings": [
                {
                    "id": 5,
                    "title": "exceptional",
                    "count": 314,
                    "percent": 56.68
                },
                {
                    "id": 4,
                    "title": "recommended",
                    "count": 145,
                    "percent": 26.17
                },
                {
                    "id": 3,
                    "title": "meh",
                    "count": 75,
                    "percent": 13.54
                },
                {
                    "id": 1,
                    "title": "skip",
                    "count": 20,
                    "percent": 3.61
                }
            ],
            "ratings_count": 545,
            "reviews_text_count": 8,
            "added": 1511,
            "added_by_status": {
                "yet": 261,
                "owned": 187,
                "beaten": 474,
                "toplay": 395,
                "dropped": 126,
                "playing": 68
            },
            "metacritic": 91,
            "suggestions_count": 346,
            "updated": "2023-04-13T20:50:14",
            "id": 52368,
            "score": None,
            "clip": None,
            "tags": [
                {
                    "id": 31,
                    "name": "Singleplayer",
                    "slug": "singleplayer",
                    "language": "eng",
                    "games_count": 214040,
                    "image_background": "https://media.rawg.io/media/games/73e/73eecb8909e0c39fb246f457b5d6cbbe.jpg"
                },
                {
                    "id": 13,
                    "name": "Atmospheric",
                    "slug": "atmospheric",
                    "language": "eng",
                    "games_count": 30180,
                    "image_background": "https://media.rawg.io/media/games/c4b/c4b0cab189e73432de3a250d8cf1c84e.jpg"
                },
                {
                    "id": 36,
                    "name": "Open World",
                    "slug": "open-world",
                    "language": "eng",
                    "games_count": 6342,
                    "image_background": "https://media.rawg.io/media/games/456/456dea5e1c7e3cd07060c14e96612001.jpg"
                },
                {
                    "id": 6,
                    "name": "Exploration",
                    "slug": "exploration",
                    "language": "eng",
                    "games_count": 19625,
                    "image_background": "https://media.rawg.io/media/games/849/849414b978db37d4563ff9e4b0d3a787.jpg"
                },
                {
                    "id": 69,
                    "name": "Action-Adventure",
                    "slug": "action-adventure",
                    "language": "eng",
                    "games_count": 13810,
                    "image_background": "https://media.rawg.io/media/games/9aa/9aa42d16d425fa6f179fc9dc2f763647.jpg"
                },
                {
                    "id": 468,
                    "name": "role-playing",
                    "slug": "role-playing",
                    "language": "eng",
                    "games_count": 1467,
                    "image_background": "https://media.rawg.io/media/games/424/424facd40f4eb1f2794fe4b4bb28a277.jpg"
                },
                {
                    "id": 37796,
                    "name": "exclusive",
                    "slug": "exclusive",
                    "language": "eng",
                    "games_count": 4512,
                    "image_background": "https://media.rawg.io/media/games/018/01857c5ff9579c48fa8bd76b4d83a946.jpg"
                },
                {
                    "id": 209,
                    "name": "Drama",
                    "slug": "drama",
                    "language": "eng",
                    "games_count": 2671,
                    "image_background": "https://media.rawg.io/media/games/b0a/b0a370527fea0e824225269d4a8797db.jpg"
                },
                {
                    "id": 3330,
                    "name": "mistery",
                    "slug": "mistery",
                    "language": "eng",
                    "games_count": 78,
                    "image_background": "https://media.rawg.io/media/screenshots/6bb/6bb352d06e9b0b4daa3555ae03b49b18.jpg"
                },
                {
                    "id": 30181,
                    "name": "horse-riding",
                    "slug": "horse-riding",
                    "language": "eng",
                    "games_count": 6,
                    "image_background": "https://media.rawg.io/media/screenshots/a00/a004d2ee33ac31981018828443c19446.jpg"
                }
            ],
            "esrb_rating": {
                "id": 3,
                "name": "Teen",
                "slug": "teen",
                "name_en": "Teen",
                "name_ru": "С 13 лет"
            },
            "user_game": None,
            "reviews_count": 554,
            "saturated_color": "0f0f0f",
            "dominant_color": "0f0f0f",
            "short_screenshots": [
                {
                    "id": -1,
                    "image": "https://media.rawg.io/media/games/5c5/5c5089af36b99bf9465357a8556449f9.jpg"
                },
                {
                    "id": 810512,
                    "image": "https://media.rawg.io/media/screenshots/146/146663905eac4dae61332bfde9e5f909.jpg"
                },
                {
                    "id": 810513,
                    "image": "https://media.rawg.io/media/screenshots/291/291fc78361a94d8d36c13efb5324a89e.jpg"
                },
                {
                    "id": 810514,
                    "image": "https://media.rawg.io/media/screenshots/ade/adeeeae07b581b8b34dcaeac2bb489c6.jpg"
                },
                {
                    "id": 810515,
                    "image": "https://media.rawg.io/media/screenshots/3e6/3e666858d666690b15cfac6a137683e1.jpg"
                },
                {
                    "id": 810516,
                    "image": "https://media.rawg.io/media/screenshots/f93/f93ae69662e4e7df19e72255616f6391.jpg"
                },
                {
                    "id": 810517,
                    "image": "https://media.rawg.io/media/screenshots/e64/e6477d591353c16cef792da9a314b98a.jpg"
                }
            ],
            "parent_platforms": [
                {
                    "platform": {
                        "id": 2,
                        "name": "PlayStation",
                        "slug": "playstation"
                    }
                }
            ],
            "genres": [
                {
                    "id": 3,
                    "name": "Adventure",
                    "slug": "adventure"
                },
                {
                    "id": 4,
                    "name": "Action",
                    "slug": "action"
                }
            ]
        }
    ],
    "user_platforms": False,
    "user_input": [
        {
            "name": "Splatoon 3",
            "rating_user": 1
        },
        {
            "name": "Ori and the Will of the Wisps",
            "rating_user": 5
        },
        {
            "name": "Sayonara Wild Hearts",
            "rating_user": 4
        },
        {
            "name": "Hades",
            "rating_user": 5
        },
        {
            "name": "Resident Evil 2",
            "rating_user": 1
        }
    ]})