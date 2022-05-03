image dano = "dano.png"
image dano_angry = "dano_angry.png"
image dano_happy = "dano_happy.png"
image dano_sad = "dano_sad.png"

image juda = "juda.png"
image juda_happy = "juda_happy.png"
image juda_sad = "juda_sad.png"

image dohwa = "dohwa.png"
image dohwa_happy = "dohwa_happy.png"
image dohwa_sad = "dohwa_sad.png"

image namju = "namju.png"
image namju_happy = "namju_happy.png"

image baek = "baek.png"
image baek_angry = "baek_angry.png"
image baek_happy = "baek_happy.png"

image haru = "haru.png"
image haru_angry = "haru_angry.png"
image haru_happy = "haru_happy.png"
image haru_sad = "haru_sad.png"

image jin = "jin.png"
image jin_angry = "jin_angry.png"
image jin_happy = "jin_happy.png"
image jin_sad = "jin_sad.png"

image book_1 = "book_1.png"
image book = "book.jpg"
image hall = "hall.png"
image kitchen = "kitchen.png"
image school = "school.png"
image library = "library.png"
image stage = "stage.png"
image classroom = "classroom.png"
image travel = "travel.png"
image bada = "bada.png"
image soup = "soup.png"
image night = "night.png"
image party = "party.png"
image swim = "swim.png"
image gym = "gym.png"
image load = "load.png"
image lobe = "lobe.png"
image tree = "tree.png"
image hospital = "hospital.png"
image gung = "gung.png"
image gung_2 = "gung_2.png"
image video = "video.png"
image stairs = "stairs.png"
image home = "home.png"
image h_room = "h_room.png"
image gung_3 = "gung_3.png"
image art = "art.png"
image s_load = "s_load.png"
image s_load_2 = "s_load_2.png"
image end = "end.png"
image university = "university.png"
image tree_2 = "tree_2.png"
image artshow = "artshow.png"
image tennis = "tennis.png"
image gung_4 = "gung_4.png"

define juda = Character('여주다', color="#ffffff")
define namju = Character('오남주', color="#ffffff")
define baek = Character('백경', color="#ffffff")
define dano = Character('은단오', color="#ffffff")
define haru = Character('하루', color="#ffffff")
define jin = Character('진미채', color="#ffffff")
define dohwa = Character('이도화', color="#ffffff")

label start:
    scene book

    play music "audio/see_the_fantasy.mp3" fadein 1.5

    "어쩌다 발견한 하루"
    "등장인물 소개"

    show dano
    dano "여 18세 "
    dano "이 드라마에서 가장 중요한 인물 중 하나는 바로 은단오 인데요. 타고나게 약한 심장을 가진 캐릭터로 고등학생의 나이에도 불구하고 벌써 여러번의 심장 수술을 겪었습니다. 다행히 유복한 집안에서 태어나 경제적인 걱정은 없지만 유약한 몸과 10년간의 짝사랑을 이어오고 있습니다."
    hide dano

    show haru
    haru "남 18세, 이름조차 없었던 순정만화 비밀의 엑스트라, 출석 번호 13번 "
    haru "조용히 학교만 다니던 캐릭터였지만 은단오를 만나게 되면서 상당한 입지를 가지게됩니다. 하루 캐릭터가 중요한 이유는 은단오, 백경과 함께 엄청난 세계의 비밀을 알아버리기 때문입니다."
    hide haru

    show baek
    baek "남 18세, 만화 비밀의 남자 조연, 스리고 서열 3위"
    baek "은단오가 10년간 짝사랑한 남자이자 약혼자. 싸가지란 찾아보려고 해야 티끌도 찾을 수 업고 늘 안하무인으로 행동합니다."
    hide baek

    show juda
    juda "여, 18세, 만화 비밀의 여자 주인공"
    juda "스리고에서 가장 핫한 입학생인 여주다는 전형적인 순정만화 속 주인공입니다. 가난하지만 마음 착하고 얼굴도 예쁜 여주인공인데요. 학교생활을 하면서 겪는 여러 갈등에서 항상 남자 주인공의 도움을 받는 캐릭터입니다"
    hide juda

    show namju
    namju "남, 18세,  만화 비밀의 남자 주인공"
    namju "이름부터 드라마 속 남주라는 것이 드러나는 만큼 오남주 또한 전형적인 드라마 속 남자 주인공의 모습을 보여줍니다. 스리고의 최고의 인기남이자 재벌 2세인 남주는 얼굴도 잘생겼는데요. 역시 전형적인 남자 주인공 답게 싸움도 잘하고 키도 큰 거만한 성격이지만 결국에는 여주다를 좋아하게 되는 캐릭터입니다."
    hide namju

    show dohwa
    dohwa "남, 18세 만화 '비밀'의 서브 남자 주인공"
    dohwa "스리고 서열 2위. 스리고 A3 서열 2위. 금수저에 얼굴도 잘생겼다. 전체적으로, 남주보다는 5\%정도 부족한 스케일이다. 무뚝뚝하고 김첨지같은 남주와는 반대로 다정하고, 애교도 많고, 장난도 잘친다"
    hide dohwa

    show jin
    jin "나이, 국적, 출신 심지어 이름까지 모든 게 비밀이다"
    jin "급식으로 진미채볶음이 나오는 날만 등장해 \'진미채 요정\'으로 불린다. 잘생긴 얼굴 하나로 스리고 학생도 아니건만 스리고 대표 존잘 중 하나로 입성한다. 작가와 가장 가까운 인물이자 가장 비밀스러운 사람이다."
    hide jin

    "스토리 시작"
    " "
    #배경
    "은단오는 어느 순간부터 정신을 차려보면 전혀 다른 상황이 펼쳐지는 현상과 함께 미래가 보이는 환상으로 인해 힘들어한다."
    scene book_1
    "어느 날 그녀는 도서관에서 반짝이고 있는 만화책을 발견하고 이를 보게 된다.\n그 책 속에는 자신이 겪었던 일들이 만화로 그려져 있었다. 그녀는 이 충격적인 일을 겪은지 얼마 되지 않아 허공에 떠있는 웜홀을 보게 된다."
    scene hall
    "이에 놀라 두리번거리며 주변을 보지만 이 희한한 광경을 보는 사람은 자신과 진미채 요정밖에 없다는 사실을 알게 된다. "
    scene kitchen
#
    stop music fadeout 1.5
    play music "audio/A Cat On The Marimba.mp3" fadein 1.5

    show dano at right
    dano "저기요! 나 알죠"
    hide dano

    show jin at right
    jin "글쎄... 어디서 봤더라?"
    hide jin

    show dano_angry at right
    dano "사색의 다리에서 같이 봤잖아요 이상한거 까맣게 막 뚫린거!"
    hide dano_angry

    show jin at right
    jin "생각보다 눈치가 빠르네.."
    jin "우린 인간이 아니야 장면과 장면 사이의 공백을 느끼는거야"
    jin "잠들지도 않았는데 다음날이 되어있고 등교한 기억이 없는데 학교에 와있고 눈 깜짝한 사이에 몇일이 지나있기도 하겠지"
    jin "평소라면 못느꼈겠지만 자아를 가지면 그 공백을 알게돼. 그리고 기억이 사라졌다고 착각하지"
    hide jin

    show dano_angry at right
    dano "기억상실증이 아니라고?"
    hide dano_angry

    show jin_happy at right
    jin "아 여긴 만화속 세상이야"
    hide jin_happy

    show dano_angry at right
    dano "미친놈... 진지하게 들은 내가 바보지"
    hide dano_angry

    show jin at right
    jin "은단오 넌 이 만화책에 등장하는 캐릭터야. 너가 본 환상도 만화의 콘티지."
    hide jin

    stop music fadeout 1.5
    play music "audio/see_the_fantasy.mp3" fadein 1.5

    scene stage
    show jin at right
    jin "우리가 있는 이 세계는 작가가 만든 만화속이야 그리고 여긴 순정만화 비밀의 공간이고"
    jin "이곳에선 작가가 의도하지 않는일은 일어나지 않아 그래서 우린 작가가 적은 말만 뱉고 이렇게 그려진대로 행동하는거지 여길 스테이지 라고 해"
    hide jin

    show dano at right
    dano "아하 그럼 여주다한테 착한척 했던것도 백경 그 싸가지한테 쩔쩔맸던 것도!"
    hide dano

    show jin at right
    jin "딩동댕! 작가가 그리지 않는 장면이나 공간들 또한 존재해. 작가가 그리지 않았으니 이상한 것들도 존재하기도 하고 여긴 섀도우지"
    jin "스테이지 밖. 즉 섀도우에선 캐릭터들이 자유로워 지금의 우리처럼 자아를 가진 캐릭터들 만이 섀도우의 일을 기억할 수가 있지."
    hide jin

    show dano_angry at right
    dano "환장하겠네"
    hide dano_angry

    show jin at right
    jin "하지만 자아를 가졌다고 해서 언제나 자유로울 수 없어 캐릭터가 어떤 행동을 하든 작가가 그린 이 스테이지대로 돌아가게 되니까"
    jin "이 세계에서는 모든게 예정대로 흘러가게 되있다는 거지 이를테면 운명..."
    hide jin

    show dano_angry at right
    dano "절대 작가 뜻대로 움직이지 않을거야 두고보면 알겠죠."
    hide dano_angry

    show jin at right
    jin "캐릭터는 작가가 정해준 대로 살 수밖에 없어. 너의 노력은 실패로 돌아가게 될거야."
    hide jin

    #선택지 스토리 시작
    scene library
    "단오는 스테이지에 올랐어도 자신이 장면의 주요 인물이 아닌 경우 자유롭게 행동할 수 있다는 점을 깨닫고 매 장면 주목받으려 행동하지만 작가의 내용 진행에 방해가 되는 순간 모든 순간이 방해되기 이전으로 초기화된다는 사실에 절망하게 된다."

    scene school
    "하지만 누군가와 마주칠 때면 자신이 본 콘티와 다른 전개가 펼쳐지게 된다는 사실을 알게 되고 그를 찾으러 온 학교를 뒤진다. "

    scene classroom
    "은단오는 콘티가 바뀔때마다 나타나는, 자신을 구해줄 그 사람을 겨우 찾게 되었다. 놀랍게도 그는 단오와 같은반 친구였던 것이다."
    "하지만 그의 존재에 대해 단오는 물론 반 친구 누구도 아는 사람이 없었다. 알고보니 그는 배역의 이름도 부여받지 못해 명찰에 이름도 없는 \"엑스트라 13번\"이라 존재감이 없었기 때문이었다."
#
    "주치의는 단오의 아버지에게 단오가 시한부 라고 말한다. 단오는 엿듣고 충격을 받지만 곧 자신의 운명을 바꾸기 위해 굳은 다짐을 한다."

    show dano at right
    dano "이따가 나랑 여주다가 과학실로 저 박스를 옮길거야 오남주 때문에 내가 저 박스를 쏟는게 정해진 이야기고"
    dano "너가 얘들 틈에 섞여서 기회를 잘 보다가 저게 안쓰러지게 딱 잡아줘 정해진 이야기를 계속 바꾸다 보면 결국엔 내 의지대로 운명도 만들 수 있는거지"
    dano "이 계획이 성공만 하면 내가 너도 책임지고 엑스트라 탈출 시켜줄게 알았지? 어?"
    hide dano

    show haru at right
    "13번" "..."
    hide haru

    show dano_angry at right
    dano "치.... 너는 왜 대답 한번을 안해주냐... 알았어 내가 도와줄게 우리같이 운명을 바꿔보자라고 해주면 안돼? 응?"
    dano "너가 무슨생각을 하는지 알수가 있어야지 아니 입을 열어서 어 그래라고 해주면 되는데 그게 그렇게 어렵니??ㅜㅜ"
    hide dano_angry

    show haru at right
    "13번" "..."
    hide haru

    " \"13번\"은 단오의 말에 아무 대답도 하지 않아 단오의 속을 태우지만 결국 단오의 요청대로 행동해 약간씩이라도 콘티를 바꾸는 결과를 가져오자 단오는 13번과 더욱 가까워질려고 한다. "
    stop music fadeout 1.5
    play music "audio/there's_a_problem.mp3" fadein 1.5

    scene travel
    "스리고의 모든 학생은 수학여행을 떠나게 된다."

    scene bada
    "첫 일정은 바닷가 구경. 단오는 이곳에서 자신이 백경에게 기념품 돌을 건네는 콘티을 본다. 백경은 그 돌을 바다에 던져버리고, 단오는 그 돌을 찾기 위해 바다로 뛰어드는 것이 콘티의 결말이다."
    "단오는 13번을 찾아가 부탁을 한다"

    show dano at right
    dano "야! 13번!"
    dano "짝사랑, 심장병 \n이게 내 설정값 정해진 이야기를 바꾸면 너도 나도 엑스트라 탈출!"
    dano "내가 있다가 바다에 빠질꺼거든? 무슨 수를 써서라도 날 막아줘 알았지??"
    hide dano

    show haru at right
    "13번" "..."
    hide haru

    $ point1 = 0

    #선택지 1번
    menu:
        "단오를 도와 단오가 바다에 빠지지 않게 한다": #하루
            $ point1 = point1 + 1
        "콘티대로 진행 시킨다": #백경
            $ point1 = point1 -1

    if(point1 == 1):
#
        show dano at right
        dano "13번 !! 너 자아가 있었구나 뭐야 왜 말 안했어"
        dano "여튼 스테이지를 바꿔줘서 고마워 ㅜㅜ"
        hide dano

        stop music fadeout 1.5
        play music "audio/Dark Side.mp3"

        scene soup
        "수학여행 첫째날\, 저녁 프로그램으로 담력훈련이 진행된다. \n제비뽑기로 담력훈련을 같이 할 짝을 뽑는데, 보나마나 작가의 의도대로 여주다와 오남주, 백경과 은단오가 짝이 된다."
        "단오는 길을 잃고 백경도 가버린 산속에서 처량하게 헤매는 콘티을 보고 지도를 달달 외우지만 작가는 무심하게도 단오를 스테이지에 올리고 심장병이 도지게 한다."
        "백경은 산속에 단오를 두고 떠나버리고\, 단오는 결국 이미 보았던 콘티대로 조난된다. 하지만 단오가 본 콘티의 결말에선 백경이 다시 찾아와 단오를 구해야 했지만 13번이 단오를 구하러 온다. "

        stop music
        play music "audio/Glow.mp3"

        scene night
        "13번은 단오를 입산통제구역으로 데려가 만화같이 예쁜 폭포와 단풍이 있는 곳을 보여준다. 둘은 이 곳에서 대화를 나누며 \"13번\"과 썸을 탄다. \"13번\"이 말도 할수 있다는 것을 알게 되자 단오는 기뻐했다."
#
        show dano_happy at right
        dano "너 덕분에 내 하루가 변할 수 있을것 같아 널 하루라고 불러도 될까\?"
        hide dano_happy

        "단오는 내 하루를 바꿔줘서 고맙다며 \'하루\'라는 이름을 지어준다."

        stop music


        scene kitchen
#
        "수학여행에서 돌아와 일상을 보내고 있는 캐릭터들."

        show dano_happy at right
        dano "저 13번한테 하루라고 이름지어 줬어요!!"
        hide dano_happy

        play music "audio/Ego.mp3"

        show jin_angry at right
        jin "이름이 없는 존재에게 이름을 붙여주면 모든게 틀어질거야."
        hide jin_angry

        scene library
        "얼마 지나지 않아 단오는 진미채 요정의 말대로 돌아가신 엄마와의 추억이 담긴 화단과 그네가 사라지고 아버지조차 기억하지 못하게 됐다는 사실을 알게 된다."
        "하지만 달라진 것은 그것뿐이 아니다. 하루 이름을 붙여준 이후로 단오가 백경에게 호감을 보내는 모습에 질투를 하게 된 것이다. 이러한 질투가 섀도우를 넘어 스테이지까지 영향을 미쳐 심지어는 백경이 하루에게 손찌검을 하기까지 한다."
        "백경은 단오에게 더이상 질투를 유발하지 말라며 다그친다. 그때 단오를 구하러온 하루."

        show baek_angry at right
        baek "너 뭐야 !!!"
        hide baek_angry

        show haru at right
        haru "말해도 기억 못해 곧 장면이 바뀌니깐"
        hide haru

        "기억 못한다는 것은 자아를 가진 캐릭터만 알고 있는 사실인데\, 하루도 자아를 가진 캐릭터라는 사실을 확실히 알게 된 단오는 충격을 받는다\. 하루의 정체는 무엇일까."
        "백경을 10년간 짝사랑해오던 단오가 백경에게 파혼을 선언하는 장면이 펼쳐지고, 이야기가 바뀐 것에 기대감을 가지게 된 단오는 이 사실을 진미채에게 말한다"

        scene kitchen
        show dano_happy at right
        dano "스테이지가 바뀌었어요 !!"
        hide dano_happy

        show jin_angry at right
        jin "이야기가 틀어지게 하지마."
        hide jin_angry

    elif(point1 == -1):
        stop music fadeout 1.5
        play music "audio/Strange Feeling.mp3" fadein 1.5
        "물에 빠진 생쥐꼴이 된 단오는 결정적인 상황에선 그도 콘티를 바꿀수 없을 것 같아 심장병으로 죽는 자신의 운명이 그대로 이루어질까봐 눈물을 흘린다."

        stop music
        play music "audio/Dark Side.mp3"

        scene soup
        "수학여행 첫째날, 저녁 프로그램으로 담력훈련이 진행된다. \n제비뽑기로 담력훈련을 같이 할 짝을 뽑는데\, 보나마나 작가의 의도대로 여주다와 오남주, 백경과 은단오가 짝이 된다."
        "단오는 길을 잃고 백경도 가버린 산속에서 처량하게 헤매는 콘티을 보고 지도를 달달 외우지만 작가는 무심하게도 단오를 스테이지에 올리고 심장병이 도지게 한다."
        "백경은 산속에 단오를 두고 떠나버리고\, 단오는 결국 이미 보았던 콘티대로 조난된다. 하지만 단오가 본 콘티의 결말에선 백경이 다시 찾아와 단오를 구해야 했지만 13번이 단오를 구하러 온다."

        stop music
        play music "audio/Glow.mp3"

        show haru at right
        "13번" "괜찮아?"
        hide haru

        show dano_happy at right
        dano "너 덕분에 내 하루가 변할 수 있을것 같아 널 하루라고 불러도 될까\?"
        hide dano_happy

        "단오는 내 하루를 바꿔줘서 고맙다며 \'하루\'라는 이름을 지어준다."

        stop music

        scene kitchen
        "수학여행에서 돌아와 일상을 보내고 있는 캐릭터들."

        show dano_happy at right
        dano "저 13번한테 하루라고 이름지어 줬어요!!"
        hide dano_happy

        play music "audio/Ego.mp3"

        show jin_angry at right
        jin "이름이 없는 존재에게 이름을 붙여주면 모든게 틀어질거야."
        hide jin_angry

        scene library
        "얼마 지나지 않아 단오는 진미채 요정의 말대로 돌아가신 엄마와의 추억이 담긴 화단과 그네가 사라지고 아버지조차 기억하지 못하게 됐다는 사실을 알게 된다."
        "하지만 달라진 것은 그것뿐이 아니다. 하루 이름을 붙여준 이후로 단오가 백경에게 호감을 보내는 모습에 질투를 하게 된 것이다. 이러한 질투가 섀도우를 넘어 스테이지까지 영향을 미쳐 심지어는 백경이 하루에게 손찌검을 하기까지 한다."
        "백경은 단오에게 더이상 질투를 유발하지 말라며 다그친다. 그때 단오를 구하러온 하루."

        show baek_angry at right
        baek "너 뭐야 !!!"
        hide baek_angry

        show haru at right
        haru "말해도 기억 못해 곧 장면이 바뀌니깐"
        hide haru

        "기억 못한다는 것은 자아를 가진 캐릭터만 알고 있는 사실인데\, 하루도 자아를 가진 캐릭터라는 사실을 확실히 알게 된 단오는 충격을 받는다\. 하루의 정체는 무엇일까."
        "백경을 10년간 짝사랑해오던 단오가 백경에게 파혼을 선언하는 장면이 펼쳐지고, 이야기가 바뀐 것에 기대감을 가지게 된 단오는 이 사실을 진미채에게 말한다"

        scene kitchen
        show dano_happy at right
        dano "스테이지가 바뀌었어요 !!"
        hide dano_happy

        show jin_angry at right
        jin "이야기가 틀어지게 하지마."
        hide jin_angry

    #선택지 2번
    $ point2 = 0
    menu:
        "말없이 수긍한다": #백경
            $ point2 = point2 + 1

        "나도 살고 싶다며 반발한다": #하루
            $ point2 = point2 - 1

    if(point2 == 1):

        scene kitchen
        "진미채도 아무말 하지 않는다"

        stop music
        play music "audio/어쩌다 발견한 코믹.mp3"

        scene party
        "남주는 생일을 며칠 앞두고 생일파티를 연다고 발표하고 반 친구들을 초청한다. 한편 단오는 콘티을 통해 생일파티의 콘티를 본다. 콘티의 결말은 남주가 주다에게 공개 고백을 하는 것. 이야기를 바꾸고 싶은 단오, "
        "자신을 모르지만 섀도우에서 단오와 있을 때마다 질투어린 신경전을 펼치는 백경에게서 단오를 지키고 싶은 하루, 주다가 남주와 공식 연인이 되는 꼴은 못보겠는 도화. 3명은 힘을 합쳐 이야기를 틀어버릴 작전을 꾸민다."
#
        show dano at right
        dano "자 집중집중! 내가 아까 말한 콘티 다들 기억하지 아무리 사소한 거라도 무언가를 변하게 해야돼 알았지?"
        hide dano

        show dohwa at right
        dohwa "근데 스테이지가 바뀌긴 할까? 스테이지가 시작될땐 모든게 제자리로 돌아가잖아"
        hide dohwa

        show dano at right
        dano "친구야 그래서 너 오남주가 여주다한테 고백하는거 그거 가만히 보고만 있을거야?"
        hide dano

        show dohwa at right
        dohwa "절대 안되지 !!"
        hide dohwa

        show dano at right
        dano "그치!! 그럼 움직여야지 어떤 이야기가 어떻게 바뀌게 될지는 모르겠지만 장면 하나씩 같이 조금이라도 바꿔야지!"
        hide dano

        "그리고 그걸 보고있는 백경은 점점 질투심을 느끼게 된다."

        stop music
        "하루는 웨이터 옷을 훔쳐입고 남주가 있는 대기실로 향한다. 하루는 남주에게 음료를 쏟아버리고 도화에게 신호를 준다."

        show haru at right
        haru "이도화! 지금이야 어서 여주다한테 가!"
        hide haru

    elif(point2 == -1):

        scene kitchen

        "하루를 찾아간 진미채"

        show jin_angry at right
        jin "이야기를 자꾸 틀어지게 하면 너의 손에 있는 흉터에서 고통이 생기고 그 고통이 점점 심해질 거야 더이상 은단오한테 호감 주지마."
        hide jin_angry

        "하루는 이 말을 듣지 않는다"

        stop music
        play music "audio/어쩌다 발견한 코믹.mp3"

        scene party
        "남주는 생일을 며칠 앞두고 생일파티를 연다고 발표하고 반 친구들을 초청한다. 한편 단오는 콘티을 통해 생일파티의 콘티를 본다. 콘티의 결말은 남주가 주다에게 공개 고백을 하는 것. 이야기를 바꾸고 싶은 단오, "
        "자신을 모르지만 섀도우에서 단오와 있을 때마다 질투어린 신경전을 펼치는 백경에게서 단오를 지키고 싶은 하루, 주다가 남주와 공식 연인이 되는 꼴은 못보겠는 도화. 3명은 힘을 합쳐 이야기를 틀어버릴 작전을 꾸민다."
#
        show dano at right
        dano "자 집중집중! 내가 아까 말한 콘티 다들 기억하지 아무리 사소한 거라도 무언가를 변하게 해야돼 알았지?"
        hide dano

        show dohwa at right
        dohwa "근데 스테이지가 바뀌긴 할까? 스테이지가 시작될땐 모든게 제자리로 돌아가잖아"
        hide dohwa

        show dano at right
        dano "친구야 그래서 너 오남주가 여주다한테 고백하는거 그거 가만히 보고만 있을거야?"
        hide dano

        show dohwa at right
        dohwa "절대 안되지 !!"
        hide dohwa

        show dano at right
        dano "그치!! 그럼 움직여야지 어떤 이야기가 어떻게 바뀌게 될지는 모르겠지만 장면 하나씩 같이 조금이라도 바꿔야지!"
        hide dano

        "그리고 그걸 보고있는 백경은 점점 질투심을 느끼게 된다."

        stop music
        "하루는 웨이터 옷을 훔쳐입고 남주가 있는 대기실로 향한다. 하루는 남주에게 음료를 쏟아버리고 도화에게 신호를 준다."

        show haru at right
        haru "이도화! 지금이야 어서 여주다한테 가!"
        hide haru

    #선택지 3번
    $ point3 = 0
    menu:
        "도화는 주다를 데리고 파티장 한구석으로 간다.": #백경
            $ point3 = point3 + 1

        "도화는 여주다에게 공개고백을 한다.": #하루
            $ point3 = point3 - 1

    if(point3 == 1):

        scene party
#
        show dohwa at right
        dohwa "주다야 너한테 꼭 하고싶은 말이 있어 좋아해"
        hide dohwa

        show juda_sad at right
        juda "나도 도화 니가 좋아 하지만 우린 친구잖아..."
        hide juda_sad

        play music "audio/Burning Light.mp3"
        "이야기가 바뀌었는데 바뀐 이야기는 이게 끝이 아니었다. 콘티의 결말은 남주가 주다에게 공개고백하는 것이었지만 바뀐 결말은 백경이 단오에게 고백하는 결말로 바뀌어버린 것이다."

        show baek at right
        baek "정식으로 선언한다. 앞으로 나한테 여자는 은단오 하나다."
        hide baek

        "결국 내용이 바뀌었지만 자아가 가진 세명이 아무도 원하지 않는 결말이 되버리고 말았다."

        stop music
        play music "audio/A Cat On The Marimba.mp3" fadein 1.5

        scene classroom
        "하루는 모든 성적에서 수준급 실력을 보여주며 반 친구들의 주목을 받는다."
        "이러면서 반에서 존재감이 생긴 하루는 결국 그 존재감이 점점 커지며 설정이 바뀌어 하루라는 진짜 이름이 생기고 반 친구들도 모두 아는 등장인물이 된다."

        scene swim
        "수영장에서 수업을 하게 된 스리고 학생들."
        "단오에게 호감이 생겨버린 백경은 같이 다닌다는 하루와 또다시 신경전을 벌인다. 갑자기 스테이지가 펼쳐지고 남주와 도화는 자존심을 건 수영대결을 하던 도중 갑자기 비상벨이 울린다."
        stop music
        "수영장에 있던 단오는 대피하는 무리에 밀려 물속에 빠지게 된다"

        show baek at right
        baek "단오야!!"
        hide baek

        "백경은 단오를 구한다"
#

        play music "audio/Take.mp3"
        scene classroom
        "다음날 단오는 학교를 가지만"
        "하루는 사라지고 반친구들은 하루가 원래 없었던 사람처럼 기억을 하지 못한다. 단오는 밖으로 나가 하루를 찾지만 충격적이게도 어디에도 보이지 않는다 "

        scene library
        "무슨 일이 일어난건지 만화책 비밀을 찾기 위해 도서관에 뛰어갔지만 비밀을 손에 들고 있던 사람은 다름 아닌 백경."

        show baek_angry at right
        baek "이거 찾나봐..? \n책을 단오 앞으로 던진다"
        hide baek_angry

        show dano at right
        dano "너... 어떻게..."
        hide dano

        show baek_angry at right
        baek "그동안 재밌었어? 아무리 설정값이라고 하지만 은단오... 섭섭하네"
        baek "캐릭터 설정 가짜 되도않는 소리까지 근데 말도 안된다고 생각했던 일들이 버젓이 일어나고 있더라고 그 책을 보는순간 모든게 납득이 됐던데"
        baek "더 웃긴게 뭔지알아? 그걸 알고있는 사람은 또 있었다는거야"
        hide baek_angry

        show dano at right
        dano "지금까지 다 알면서 일부러..."
        hide dano

        show baek_angry at right
        baek "먼저 사람 바보 만든게 누군데"
        hide baek_angry
#
        "백경이 자아를 찾아버리고 만화책을 통해 모든 상황을 알아버린 것이다. 백경은 언제부터 자아를 찾았던걸까."
        "단오는 만화책 속에 하루가 모두 사라져있자 충격을 받는다."

        scene kitchen
#
        show dano_sad at right
        dano "하루가 사라졌어요"
        hide dano_sad

        show jin_angry at right
        jin "틀어지는게 아니었어 결국 제자리로 돌아오고 있었던거야"
        hide jin_angry

        show dano_sad at right
        dano "다시는 이야기를 바꾸지 않을게요 ㅜㅜㅜ 제발 하루가 어딨는지 알려주세요"
        hide dano_sad

        show jin_angry at right
        jin "..."
        hide jin_angry

        scene classroom
        "도화는 하루가 사라져 충격을 받은 단오의 모습을 보고 주다를 향한 마음을 접는다"
        "백경은 비록 지금까지는 설정값 때문에 단오에게 쌀쌀맞게 대했지만 자아를 찾은 지금이라도 단오의 마음을 잡아보려 노력한다."

        stop music
        scene gym
        "스리고 운동회가 열린다. 스테이지가 열리고 단오와 백경은 함께 경기에 커플로 참가한다."
        "스테이지 속 단오는 여전히 백경을 짝사랑하고 백경은 여전히 단오에게 쌀쌀맞게 군다."
        "경기에 참가한다 단오가 발을 헛디뎌 넘어지는데 스테이지가 꺼진다. 그 순간 누군가 나타나 단오를 도와주는데, 그 사람은 바로 하루다."
        "하지만 다시 나타난 하루는 백경을 따르는 '그 외 등장인물'로 새로 등장한 캐릭터일 뿐이다. 단오와의 추억도 사랑도 모두 기억하지 못한다. "
        "백경은 새로 나타난 하루가 위협이 되지 않는다고 생각한다."

        scene classroom
#
        "백경은 시한부 인생을 바꿔보려는 의지가 꺾인 단오에게 함께 설정을 바꾸자며 자신의 자아 속 진짜 마음을 전한다."
        show baek at right
        baek "나랑 같이 설정을 바꿔보자"
        hide baek

    elif(point3 == -1):

        play music "audio/Yellow Sky.mp3"
        scene party
        show dohwa at right
        dohwa "정식으로 선언한다 앞으로 나한테 여자는 여주다 하나다."
        hide dohwa

        show juda_sad at right
        juda "나도 도화 니가 좋아 하지만 우린 친구잖아..."
        hide juda_sad

        "정해진 콘티가 바뀌게 되고 세사람 모두 만족하는 결과가 나타나게 된다."

        stop music
        play music "audio/A Cat On The Marimba.mp3" fadein 1.5

        scene classroom
        "하루는 모든 성적에서 수준급 실력을 보여주며 반 친구들의 주목을 받는다."
        "이러면서 반에서 존재감이 생긴 하루는 결국 그 존재감이 점점 커지며 설정이 바뀌어 하루라는 진짜 이름이 생기고 반 친구들도 모두 아는 등장인물이 된다."

        scene swim
        "수영장에서 수업을 하게 된 스리고 학생들. 심장병이 있는 단오는 엑스트라라 수영수업조차 받지 못하는 하루와 물밖에서 물장구나 치면서 놀고 있다."
        "단오에게 호감이 생겨버린 백경은 같이 다닌다는 하루와 또다시 신경전을 벌인다. 갑자기 스테이지가 펼쳐지고 남주와 도화는 자존심을 건 수영대결을 하던 도중 갑자기 비상벨이 울린다."
        stop music

        "수영장에 있던 단오는 대피하는 무리에 밀려 물속에 빠지게 된다"


        show haru at right
        haru "단오야!!"
        hide haru

        "하루는 단오를 구한다"

        scene hospital
        "병원에서 깨어난 단오\n병실에는 백경만 있을 뿐이다."

        play music "audio/Take.mp3"
        scene classroom
        "다음날 단오는 학교를 가지만"
        "하루는 사라지고 반친구들은 하루가 원래 없었던 사람처럼 기억을 하지 못한다. 단오는 밖으로 나가 하루를 찾지만 충격적이게도 어디에도 보이지 않는다 "

        scene library
        "무슨 일이 일어난건지 만화책 비밀을 찾기 위해 도서관에 뛰어갔지만 비밀을 손에 들고 있던 사람은 다름 아닌 백경."

        show baek_angry at right
        baek "이거 찾나봐..? \n책을 단오 앞으로 던진다"
        baek "급하긴 했나봐 그꼴로 여기까지"
        hide baek_angry

        show dano at right
        dano "너... 어떻게..."
        hide dano

        show baek_angry at right
        baek "그동안 재밌었어? 10년간 날 짝사랑 했다면서 일일이 얘기를 해줘야 아는거야? 아무리 설정값이라고 하지만 은단오... 섭섭하네"
        baek "난 처음에 무슨 일인가 싶었어 10년동안 귀찮게 하더니 갑자기 파혼?"
        baek "캐릭터 설정 가짜 되도않는 소리까지 근데 말도 안된다고 생각했던 일들이 버젓이 일어나고 있더라고 그 책을 보는순간 모든게 납득이 됐던데"
        baek "더 웃긴게 뭔지알아? 그걸 알고있는 사람은 또 있었다는거야 재밌더라고 엑스트라 주제에 발악하는 모습이"
        hide baek_angry

        show dano at right
        dano "지금까지 다 알면서 일부러..."
        hide dano

        show baek_angry at right
        baek "먼저 사람 바보 만든게 누군데"
        hide baek_angry

        "백경이 자아를 찾아버리고 만화책을 통해 모든 상황을 알아버린 것이다. 백경은 언제부터 자아를 찾았던걸까."
        "단오에게 자신을 가지고 놀아 좋냐며 비아냥대는 백경에게 만화책을 받아든 단오는 만화책 속에 하루가 모두 사라져있자 충격을 받는다."

        scene kitchen
        show dano_sad at right
        dano "하루가 사라졌어요"
        hide dano_sad

        show jin_angry at right
        jin "틀어지는게 아니었어 결국 제자리로 돌아오고 있었던거야"
        hide jin_angry

        show dano_sad at right
        dano "다시는 이야기를 바꾸지 않을게요 ㅜㅜㅜ 제발 하루가 어딨는지 알려주세요"
        hide dano_sad

        show jin_angry at right
        jin "..."
        hide jin_angry

        scene classroom
        "도화는 하루가 사라져 충격을 받은 단오의 모습을 보고 주다를 향한 마음을 접는다"
        "백경은 비록 지금까지는 설정값 때문에 단오에게 쌀쌀맞게 대했지만 자아를 찾은 지금이라도 단오의 마음을 잡아보려 노력한다. 하지만 10년간의 짝사랑을 이어온 단오의 모습은 그저 스테이지 속에만 있고 자아를 가진 단오에겐 없다는 걸 느끼게 되자 좌절감을 가진다."

        stop music
        scene gym
        "스리고 운동회가 열린다. 스테이지가 열리고 단오와 백경은 함께 경기에 커플로 참가한다."
        "스테이지 속 단오는 여전히 백경을 짝사랑하고 백경은 여전히 단오에게 쌀쌀맞게 군다."
        "경기에 참가한다 단오가 발을 헛디뎌 넘어지는데 스테이지가 꺼진다. 그 순간 누군가 나타나 단오를 도와주는데, 그 사람은 바로 하루다."
        "하지만 다시 나타난 하루는 백경을 따르는 '그 외 등장인물'로 새로 등장한 캐릭터일 뿐이다. 단오와의 추억도 사랑도 모두 기억하지 못한다. "
        "백경은 새로 나타난 하루가 위협이 되지 않는다고 생각한다"

        scene classroom
        "백경은 시한부 인생을 바꿔보려는 의지가 꺾인 단오에게 함께 설정을 바꾸자며 자신의 자아 속 진짜 마음을 전한다."
        show baek at right
        baek "나랑 같이 설정을 바꿔보자"
        hide baek

    #선택지 4번
    $ point4 = 0
    menu:
        "수락한다.": #백경
            $ point4 = point4 + 1

        "거절한다": #하루
            $ point4 = point4 - 1

    if(point4 == 1):

        scene classroom
#
        "오늘도 스리고 최고 인기남 남주와 썸을 타고 있는 데다 가난한 집안에 부모 없는 주다는 괴롭힘을 당한다. 그런 모습을 본 남주는 도저히 참을 수 없다는 듯 방송실로 달려가 주다에게 공개 고백을 한다. "
        "생일파티의 결말을 바뀌었지만 결국 하루의 기억만 잃어버리고 자신의 콘티와 별다를 것 없는 이야기가 펼쳐지자 시한부 설정값을 바꾸고 싶었던 단오와, 주다와 커플이 되고 싶던 도화는 결국 작가의 의도를 바꾸려는 의지를 버린다."

        play music "audio/Take.mp3"
        scene kitchen
        "한편, 진미채는 '비밀' 말고도 '능소화'란 만화책을 가지고 있다. 비밀보다 오래된 만화책 같은데 우연히 능소화를 발견한 하루가 책을 집어 들자 뺏어가버리지 않나, 백경이 책을 몇 장 읽은 걸 보자 불같이 화를 내지 않나. "
        "능소화에는 단오, 백경, 하루와 똑같은 얼굴들의 캐릭터가 등장하고 있다. 아무래도 이 책이 뭔가 큰 비밀을 숨기고 있는 것 같다."
        jin "진작에 태웠어야 했는데.."

    elif(point4 == -1):

        scene classroom
#
        "하지만 백경과의 마음이 무심하게도 드라마에선 자신과는 전혀 관련도 없는 백경의 약혼녀 단오에게 끌리는 하루, 내 눈앞에 나타난 하루는 내가 알던 하루와 전혀 다른 사람이라는 걸 알면서도 마음이 가는 단오의 모습이 그려진다."
        "오늘도 스리고 최고 인기남 남주와 썸을 타고 있는 데다 가난한 집안에 부모 없는 주다는 괴롭힘을 당한다. 그런 모습을 본 남주는 도저히 참을 수 없다는 듯 방송실로 달려가 주다에게 공개 고백을 한다. "
        "생일파티의 결말을 바뀌었지만 결국 하루의 기억만 잃어버리고 자신의 콘티와 별다를 것 없는 이야기가 펼쳐지자 시한부 설정값을 바꾸고 싶었던 단오와, 주다와 커플이 되고 싶던 도화는 결국 작가의 의도를 바꾸려는 의지를 버린다."

        play music "audio/Take.mp3"
        scene kitchen
        "한편, 진미채는 '비밀' 말고도 '능소화'란 만화책을 가지고 있다. 비밀보다 오래된 만화책 같은데 우연히 능소화를 발견한 하루가 책을 집어 들자 뺏어가버리지 않나, 백경이 책을 몇 장 읽은 걸 보자 불같이 화를 내지 않나. "
        "능소화에는 단오, 백경, 하루와 똑같은 얼굴들의 캐릭터가 등장하고 있다. 아무래도 이 책이 뭔가 큰 비밀을 숨기고 있는 것 같다."
        jin "진작에 태웠어야 했는데.."

    #선택지 5번
    $ point5 = 0
    menu:
        "능소화를 불태워버린다.": #백경
            $ point5 = point5 + 1

        "불태우지 않는다": #하루
            $ point5 = point5 - 1

    if(point5 == 1):
        stop music
        scene classroom
        "하루는 자신을 하루가 아니라고 하는 단오의 말에 자꾸 마음이 쓰인다."
#
        "한편, 백경이 단오에게 말을 건다."

        show baek at right
        baek "내가 기억하는 은단오들은 진짜냐 가쨔냐"
        hide baek

        show dano at right
        dano "나도 이제 모르겠어 하지만 내가 자아를 찾기 전까지는 진짜였어"
        hide dano

        "백경은 단오의 말에 내심 다행이라고 생각한다."

        play music "audio/Strange Feeling.mp3"
        scene load
        "단오는 이 세상과 길거리를 다니는 이렇게 많은 사람들이 엑스트라라는 것에 정체성의 혼란을 느끼며 길거리를 헤매고 있다"
        "혼란스러운 울음을 삼키며 길거리에 서있는데, 뒤에서 익숙한 목소리가 들린다."

        show haru_sad at right
        haru "이번엔 내가 네 이야기를 바꾸러 왔어 은단오 미안해 내가 너무 늦게 왔지"
        hide haru_sad

        "기억을 다시 찾은 하루를 본 단오는 다행이라고 생각한다."

        scene library
        "하루가 기억을 찾는 과정"
        "하루는 도서관에서 우연히 블랙홀을 보게 된다. 그 블랙홀에서는 전작 '능소화'의 장면들이 보이고 있다. 하루가 손을 뻗는 순간 모든 기억이 떠오르게 된다."
        "하루는 기억을 되찾고 단오를 찾아오게 된다. 단오는 다시는 운명을 바꾸려는 시도를 하지 않겠다고 다짐한다."

        stop music
        play music "audio/Solitude.mp3"
        scene classroom
        "수업받기 지루한 단오와 백경은 섀도우임을 이용해 선생님 앞에서 대놓고 땡땡이를 친다. 단오와 백경은 평소에 가보지 않은 골목을 가본다. 그 골목에는 예쁜 가게들이 많지만 그저 만화 속 배경으로 쓰이는 가게들인지 그곳들엔 다들 주인도 없다."

        "마치 세트장 같은 그 가게들에서 즐거운 추억을 쌓는다."
        "자아를 찾은 백경은 자신을 짝사랑하던 단오를 하루에게 빼앗겼다고 생각하는지 자신의 우월적인 설정값을 운운하며 설정값대로 그냥 자신을 따르라며 하루를 견제하는 발언으로 신경전을 벌인다. "
        "하지만 하루는 이를 전혀 개의치 않아 한다."

        stop music
        scene kitchen
        "진미채는 태워버린 능소화의 잿더미를 다시 찾아보며 완벽하게 태웠다 안심한다. 하지만 백경은 그 잿더미 속에서 타지 않은 만화책의 조각들을 본다."
#
        play music "audio/Get In.mp3"
        show baek_angry at right
        baek "이 책 뭐에요?"
        hide baek_angry

        show jin_angry at right
        jin "이미 집필이 끝난 책은 이야기를 바꿀 힘이 없어."
        hide jin_angry

        "전작인 '능소화' 속에서 캐릭터들이 자아를 가지면서 이야기가 바뀌고 이로 인해 비극적인 결말에 이르렀으며 진미채는 그 속에서 모든 상황을 지켜본 것으로 보인다."

        scene lobe
        "단오의 스마트워치가 갑자기 울리기 시작한다."
#
        show dano_angry at right
        dano "어? 이게 왜이러지 나 안아파!"
        hide dano_angry

        show haru at right
        haru "곧 스테이지가 시작될거야 너가 쓰러지겠지 스마트워치 풀어봐"
        hide haru

        "스마트워치를 푸는 단오"

    elif(point5 == -1):

        stop music
        scene classroom
        "하루는 자신을 하루가 아니라고 하는 단오의 말에 자꾸 마음이 쓰인다."
#
        "한편, 백경과 단오는 대화를 한다."

        show dano_angry at right
        dano "내가 널 좋아하는 건 설정값일 뿐이야 그러니까 쉐도우에서 억지로 연기할 필요 없어"
        hide dano_angry

        show baek at right
        baek "내가 기억하는 은단오들은 진짜냐 가쨔냐"
        hide baek

        show dano_angry at right
        dano "나도 이제 모르겠어 근데 확실한건 앞으로 그려질 모든 장면의 은단오는 작가의 뜻 그이상 그 이하도 아니야"
        hide dano_angry

        "백경은 단오가 스테이지에서 보여주는 단오의 호감 어린 행동은 모두 설정값일뿐 하나도 진짜가 없다는 단오의 말에 깊은 실망을 느낀다."

        play music "audio/Strange Feeling.mp3"
        scene load
        "단오는 이 세상과 길거리를 다니는 이렇게 많은 사람들이 엑스트라라는 것에 정체성의 혼란을 느끼며 길거리를 헤매고 있다"
        "혼란스러운 울음을 삼키며 길거리에 서있는데, 뒤에서 익숙한 목소리가 들린다."

        show haru_sad at right
        haru "이번엔 내가 네 이야기를 바꾸러 왔어 은단오 미안해 내가 너무 늦게 왔지"
        hide haru_sad

        "기억을 다시 찾은 하루를 본 단오는 기쁨의 눈물을 흘리고 하루는 단오를 꼭 안아준다."

        scene library
        "하루가 기억을 찾는 과정"
        "하루는 도서관에서 우연히 블랙홀을 보게 된다. 그 블랙홀에서는 전작 '능소화'의 장면들이 보이고 있다. 하루가 손을 뻗는 순간 모든 기억이 떠오르게 된다."
        "하루는 기억을 되찾고 단오를 찾아오게 된다. 단오는 기쁨의 눈물을 흘리며 다시는 운명을 바꾸려는 시도를 하지 않겠다고 다짐한다."

        stop music
        play music "audio/Solitude.mp3"
        scene classroom
        "수업받기 지루한 단오와 하루는 섀도우임을 이용해 선생님 앞에서 대놓고 땡땡이를 친다. 단오와 하루는 평소에 가보지 않은 골목을 가본다. 그 골목에는 예쁜 가게들이 많지만 그저 만화 속 배경으로 쓰이는 가게들인지 그곳들엔 다들 주인도 없다."

        "마치 세트장 같은 그 가게들에서 즐거운 추억을 쌓는다. 하루는 단오와 데이트를 하며 자꾸 전작 '능소화' 속 사극 장면들을 데자뷰 처럼 보게 된다."
        "자아를 찾은 백경은 자신을 짝사랑하던 단오를 하루에게 빼앗겼다고 생각하는지 자신의 우월적인 설정값을 운운하며 설정값대로 그냥 자신을 따르라며 하루를 견제하는 발언으로 신경전을 벌인다. "
        "하지만 하루는 이를 전혀 개의치 않아 하고 단오와 도화는 자아도 찾았는데 꼭 설정값 속 성격대로 성질을 부리고 다녀야겠냐며 타박하는 걸 보면 아무래도 백경은 단오의 마음을 되찾기는 어려울 것 같아 보인다."

        stop music
        "백경은 언뜻 본 그 전작 만화 '능소화'의 비밀을 찾으려 한다."

        scene library
        "도서관에서 능소화 책을 찾아본다"

        scene kitchen
#
        play music "audio/Get In.mp3"
        show baek_angry at right
        baek "이 책 뭐에요?"
        hide baek_angry

        show jin_angry at right
        jin "이미 집필이 끝난 책은 이야기를 바꿀 힘이 없어."
        hide jin_angry

        "전작인 '능소화' 속에서 캐릭터들이 자아를 가지면서 이야기가 바뀌고 이로 인해 비극적인 결말에 이르렀으며 진미채는 그 속에서 모든 상황을 지켜본 것으로 보인다."

        scene lobe
        "단오의 스마트워치가 갑자기 울리기 시작한다."
#
        show dano_angry at right
        dano "어? 이게 왜이러지 나 안아파!"
        hide dano_angry

        show haru at right
        haru "곧 스테이지가 시작될거야 너가 쓰러지겠지 스마트워치 풀어봐"
        hide haru

        "스마트워치를 푸는 단오"

    #선택지 6번
    $ point6 = 0
    menu:
        "스마트워치를 풀어 옆에 있던 세미의 손목에 끼워준다.": #하루
            $ point6 = point6 + 1

        "스마트워치를 풀어서 던져버린다.": #백경
            $ point6 = point6 - 1

    if(point6 == 1):

        scene lobe
        "쓰러진 누군가를 구하러 백경이 나타나는데, 정작 쓰러진 사람의 얼굴을 보니 단오가 아니라 세미다. 백경이 스테이지에 묶인 사이 하루는 백경의 눈앞에서 단오를 빼돌린다."

        stop music
        play music "audio/Yellow Sky.mp3"
        scene tree
        "학교엔 며칠 뒤인 10월 10일에 3백 번째 생일을 맞는다는 아름드리나무가 있다."

        show haru_happy at right
        haru "우리가 스테이지에 있든 쉐도우에 있든 10월 10일에 거기서 만나자 그러면 왠지 저 나무처럼 우리도 오래 같이 있을것만 같아서"
        hide haru_happy

    elif(point6 == -1):

        scene lobe
        "스테이지가 시작되고 다른 대체될 사람이 없던 스마트워치는 다시 단오의 손목에 채워지게 되고 쓰러진 단오를 구하러 백경이 나타난다."

        stop music
        play music "audio/Yellow Sky.mp3"
        scene tree
        "학교엔 며칠 뒤인 10월 10일에 3백 번째 생일을 맞는다는 아름드리나무가 있다."

        show haru_happy at right
        haru "우리가 스테이지에 있든 쉐도우에 있든 10월 10일에 거기서 만나자 그러면 왠지 저 나무처럼 우리도 오래 같이 있을것만 같아서"
        hide haru_happy

#선택지 추가
    $ point = 0
    menu:
        "수락한다": #하루
            $ point = point + 1

        "거절한다": #백경
            $ point = point - 1

    if(point == 1):
        stop music
        play music "audio/Burning Light.mp3"
        scene hospital
        "하지만 작가는 무심하게도 단오를 10월 10일 당일에 스테이지로 소환한다. 소환된 곳은 학교와 거리가 먼 병원의 입원실이다. 하루는 하루 종일 나무 앞에서 기다리지만 결국 단오를 만나지 못하게 된다. 아직도 스테이지에 잡혀 있는 단오."
        "하루는 10월 17일에서야 도화로부터 단오가 입원 중이란 이야기를 전달받게 되지만 하루가 병원으로 달려갈 때마다 병원은 엑스트라가 갈수 없는 곳이라는 듯 스테이지로 소환되버린다."
        scene tree
        stop music
        play music "audio/Perfume.mp3"
        "스테이지에 갇혀 10월 31일이 돼서야 풀려난 단오. 이제서야 풀려난 단오는 바로 아름드리나무로 달려가고, 병원도 가지 못해 학교에서 기다리던 하루와 재회한다. 하루는 단오에게 사랑의 고백을 하고, 둘은 서로에게 이끌려 자연스레 입술을 맞추게 된다."
        scene hospital
        "백경은 사실 단오가 입원해 있던 몇 주간 매일같이 단오가 깨어나길 바라며 꽃다발을 가지고 병문안을 왔다. "
        "백경은 단오가 떠난 빈 병실에서 병실에 입원해있던 단오와 쌓았던 어린 시절을 회상한다"
        scene library
        stop music
#
        show baek at right
        baek "니말이 맞던데 스테이지를 막 바꾸고 하루 걔. 스테이지를 바꾸면 아무나 좋아하는 거였냐?"
        hide baek

    elif(point == -1):
        stop music
        play music "audio/Burning Light.mp3"
        scene hospital
        "작가는 단오를 10월 10일 당일에 스테이지로 소환한다. 소환된 곳은 학교와 거리가 먼 병원의 입원실이다."
        "아직도 스테이지에 잡혀 있는 단오. 하루는 10월 17일에서야 도화로부터 단오가 입원 중이란 이야기를 전달받게 되지만 하루가 병원으로 달려갈 때마다 스테이지로 소환되버린다."
        stop music
        play music "audio/Perfume.mp3"
        "스테이지에 갇혀 10월 31일이 돼서야 풀려난 단오."
        "백경은 사실 단오가 입원해 있던 몇 주간 매일같이 단오가 깨어나길 바라며 꽃다발을 가지고 병문안을 왔다. "
        "단오와 백경은 병실에 입원해있던 단오와 쌓았던 어린 시절을 회상한다."

        scene library
        stop music
        show baek at right
        baek "니말이 맞던데 스테이지를 막 바꾸고 하루 걔. 스테이지를 바꾸면 아무나 좋아하는 거였냐?"
        hide baek

    #선택지 7번
    $ point7 = 0
    menu:
        "좋아한다고 대답한다": #하루
            $ point7 = point7 + 1

        "아직 잘 모르겠다고 대답한다": #백경
            $ point7 = point7 - 1

    if(point7 == 1):

        scene library
        play music "audio/there's_a_problem.mp3"
        show dano_sad at right
        dano "맞아 처음엔 그랬어 하루랑 같이 있으면 스테이지가 바뀌니까 어떻게든 내 시한부 설정값좀 바꿔보고 싶어서"
        hide dano_sad

        show  baek_angry at right
        baek "그래서 막 바꿔서 뭐 그래봤자 걔랑 너랑 그냥.. "
        hide baek_angry

        show dano_angry at right
        dano "그냥 뭐 엑스트라라고? 그래 뭐 그것도 맞네 난 계속 엑스트라고 설정값도 그대로지만 이젠 상관없어 하루는 나한테 아무나가 아니니까  하루랑 같이 있으면 매순간을 주인공으로 만들어준다고. 이세계에서 내가 무슨 역할이든 상관없어 하루랑 난 장면밖에서 이미 충분히 행복하니까"
        hide dano_angry

        stop music
        play music "audio/Dark Side.mp3"
        scene gung_4
        "본격적으로 '능소화'의 이야기가 나온다. 진미채의 회상. '능소화'의 배경은 고려 시대인 것 같다. 왕이 죽고 왕세자인 진미채가 새로운 왕이 된다."
        "후궁의 아들 백경은 진미채의 약점, 진미채의 어머니인 대비마마가 선대 왕의 사랑을 독차지하기 위해 백경의 엄마인 후궁을 독살했다는 사실을 쥐고 왕인 진미채를 위협한다."
        "진미채는 왕을 하기엔 너무 심약하지만 대비마마은 아들을 이용해 대비마마 자리에 앉아있을 생각만 하고 있어 진미채를 괴롭게 한다."

        scene gung
        "백경은 호위무사인 하루를 데리고 '비밀'에서 백경 아빠를 맡고 있는 백대성과 함께 반역을 준비한다."
        "백경은 '비밀'에서 단오의 아빠를 맡고 있는 충신 은무영을 포섭하기 위해 약점을 찾아오라 하루에게 지시한다"

        show baek at right
        baek "은무영의 약점을 찾아라"
        hide baek

        scene gung_2

        stop music
        "하루의 환상"
        "하루는 은무영의 딸 '은단오'의 마음을 얻어야 한다 보고한다."
        "백경은 우연을 가장한 상황들을 만들어 단오의 마음을 얻으려 한다. 결국 단오는 백경의 정혼자가 된다. 하지만 그 모습을 곁에서 지켜보던 하루는 순수한 은단오가 이용당하는 게 안타까운 눈빛이다."

        show dano at right
        dano "나 결혼 안할래 백경이 싫어졌어 그러니깐 백경 너도 오기싫은 병원 오지마"
        dano "아빠 나 파혼할래"
        hide dano

        "단오는 마음 없는 사랑을 하던 백경의 모습에 파혼을 하겠다 말하고 백경은 달래느라 진땀을 뺀다. 백경은 단오의 환심을 사려 하루를 통해 별 보기 좋은 장소를 찾고, 백경은 단오를 그곳으로 부른다. 이 곳에서 별을 보여주며 다시 마음을 얻는다. "
        "하지만 이는 스테이지의 내용이었을 뿐 하루와 단오는 '능소화'에서도 자아를 찾게 된다 하루는 어느 날부터 자신의 기억이 사라지고 갑자기 자신이 원하지 않는 행동을 하고 있다는 걸 느끼게 된다."
        "또한 우연히 얻게 된 '능소화'란 서책에 자신의 행동이 그대로 적혀가고 있다는 사실에 혼란스러워한다. 그러던 중 자신이 모시던 백경의 정인인 은단오가 장면이 바뀌는 걸 인지하고 있는 걸 알게 되자 그 사실을 공유하게 된다."
        "둘은 이 혼란한 감정에 대한 동질감을 가지면서 점점 더 가까워진다. 단오도 백경과 혼인하기 정말 싫지만 이게 운명이라는 사실에 좌절한다."

        scene kitchen
        "하루는 진미채를 찾아가 자신에게 자꾸 보이는 환상에 대해 묻는다."
        "하지만 진미채는 전작에 대한 기억을 찾을수록 괴로워질 뿐이다, 너와 단오는 절대 이루어질 수 없다, 비극을 막으려면 스테이지를 막으려는 단오를 막으라는 답을 할 뿐이다."

        scene classroom
        "단오와 결혼하는 설정을 바꾸기 싫었던 백경은 스테이지를 바꾸려는 하루의 모든 시도를 막아내리라 다짐한다."

        scene video
#
        play music "audio/A Cat On The Marimba.mp3"
        "단오, 오랜만에 콘티를 본다. 환상 속 배경은 스리고 영상제다."
        show dano_sad at right
        dano "나 백경한테 고백받을꺼 같아 오랜만에 본 콘티가 하필.. 작가가 기어코 백경이랑 나를 결혼시킬껀가봐 "
        dano "사실 나 백경이랑 결혼하기 싫어"
        hide dano_sad

        show haru_happy at right
        haru "단오야 바꿀래?"
        hide haru_happy
        "백경이 단오에게 프러포즈 하는 꼴은 못 보는 하루. 스테이지가 시작되고 무대에선 백경이 준비한 영상이 방영되려고 한다"

    elif(point7 == -1):

        scene gung_4
        play music "audio/Dark Side.mp3"
        "본격적으로 '능소화'의 이야기가 나온다. 진미채의 회상. '능소화'의 배경은 고려 시대인 것 같다. 왕이 죽고 왕세자인 진미채가 새로운 왕이 된다."
        "후궁의 아들 백경은 진미채의 약점, 진미채의 어머니인 대비마마가 선대 왕의 사랑을 독차지하기 위해 백경의 엄마인 후궁을 독살했다는 사실을 쥐고 왕인 진미채를 위협한다."
        "진미채는 왕을 하기엔 너무 심약하지만 대비마마은 아들을 이용해 대비마마 자리에 앉아있을 생각만 하고 있어 진미채를 괴롭게 한다."

        scene gung
        "백경은 호위무사인 하루를 데리고 '비밀'에서 백경 아빠를 맡고 있는 백대성과 함께 반역을 준비한다. 백경은 '비밀'에서 단오의 아빠를 맡고 있는 충신 은무영을 포섭하기 위해 약점을 찾아오라 하루에게 지시한다"

        scene gung_2
        stop music
        "다음은 하루의 환상. 하루는 은무영의 딸 '은단오'의 마음을 얻어야 한다 보고하고, 백경은 우연을 가장한 상황들을 만들어 단오의 마음을 얻으려 한다. 결국 단오는 백경의 정혼자가 된다. 하지만 그 모습을 곁에서 지켜보던 하루는 순수한 은단오가 이용당하는 게 안타까운 눈빛이다."
        "단오는 마음 없는 사랑을 하던 백경의 모습에 파혼을 하겠다 말하고 백경은 달래느라 진땀을 뺀다. 백경은 단오의 환심을 사려 하루를 통해 별 보기 좋은 장소를 찾고, 백경은 단오를 그곳으로 부른다. 이 곳에서 별을 보여주며 다시 마음을 얻는다. "
        "하지만 이는 스테이지의 내용이었을 뿐 하루와 단오는 '능소화'에서도 자아를 찾게 된다 하루는 어느 날부터 자신의 기억이 사라지고 갑자기 자신이 원하지 않는 행동을 하고 있다는 걸 느끼게 된다."
        "또한 우연히 얻게 된 '능소화'란 서책에 자신의 행동이 그대로 적혀가고 있다는 사실에 혼란스러워한다. 그러던 중 자신이 모시던 백경의 정인인 은단오가 장면이 바뀌는 걸 인지하고 있는 걸 알게 되자 그 사실을 공유하게 된다."
        "둘은 이 혼란한 감정에 대한 동질감을 가지면서 점점 더 가까워진다. 단오도 백경과 혼인하기 정말 싫지만 이게 운명이라는 사실에 좌절한다."

        scene kitchen
        "하루는 진미채를 찾아가 자신에게 자꾸 보이는 환상에 대해 묻는다. 하지만 진미채는 전작에 대한 기억을 찾을수록 괴로워질 뿐이다, 너와 단오는 절대 이루어질 수 없다, 비극을 막으려면 스테이지를 막으려는 단오를 막으라는 답을 할 뿐이다."

        scene classroom
        "단오와 결혼하는 설정을 바꾸기 싫었던 백경은 스테이지를 바꾸려는 하루의 모든 시도를 막아내리라 다짐한다."

        scene video
        play music "audio/A Cat On The Marimba.mp3"
        "단오, 오랜만에 콘티를 본다. 환상 속 배경은 스리고 영상제다."

        show dano_sad at right
        dano "나 백경한테 고백받을꺼 같아 오랜만에 본 콘티가 하필.. 작가가 기어코 백경이랑 나를 결혼시킬껀가봐 "
        dano "사실 나 백경이랑 결혼하기 싫어"
        hide dano_sad

        show haru at right
        haru "단오야 바꿀래?"
        hide haru
        "백경이 단오에게 프러포즈 하는 꼴은 못 보는 하루. 스테이지가 시작되고 무대에선 백경이 준비한 영상이 방영되려고 한다"

    #선택지 11번
    $ point8 = 0
    menu:
        "방송실에서 컨트롤러의 전원을 뽑아버린다.": #하루
            $ point8 = point8 + 1

        "직접 무대로 가서 막는다.": #백경
            $ point8 = point8 - 1

    if(point8 == 1):
        stop music
        scene video
        "무대는 암전 되고 곧바로 스테이지가 다시 시작된다. 도화가 섀도우에서 영상 USB를 바꿔치기하자 새로운 스테이지는 단오반의 양아치인 양일이 일진에게 프러포즈 하는 내용으로 변해버린다."

        play music "audio/Burning Light.mp3"
        scene library
        "스테이지를 기대했던 백경은 하루가 스테이지를 바꿔왔던 모습을 떠올리면서 그 비법을 짐작하게 된다. 스테이지는 생각보다 완벽하지 않으므로 하루는 엑스트라라 설정값이 없어서 스테이지에 들어가기도 쉬웠다는 걸 알게 된다."
        "또한 스테이지를 바꾸는 두 가지 규칙을 찾아내게 되는데, 하나는 섀도우에서 만든 상황이 스테이지에 영향을 끼친다는 것. 다른 하나는 스테이지를 진행할 대체자가 있다면 스테이지에서 빠져나올 수 있다는 것."
        show baek at right
        baek "스테이지가 시작된다고 모든게 원래대로 돌아가는게 아니었어 섀도우에서 만든 상황이 스테이지에서 영향을 끼쳤고, 마지막으로 필요한건 스테이지를 진행할 대체자."
        "어쩌면 자신도 무언가 일을 꾸밀 수 있을 것 같다는 묘한 표정을 짓는다."
        hide baek
        stop music

        play music "audio/A Door To Time.mp3"
        scene classroom
        "단오는 자신이 수술을 받으며 사망하는 콘티를 본다."

        show dano_sad at right
        dano "내가.. 죽어..?"
        hide dano_sad

        show haru_sad at right
        haru "단오야 왜그래"
        hide haru_sad

        show dano_sad at right
        dano "잠깐만...(하루에게 안긴다)"
        hide dano_sad
        stop music

        scene gung_2
        play music "audio/Ego.mp3"
        "하루는 '능소화'의 환상을 본다. 기억의 조각들이라 자세한 내용은 알긴 어렵다. '능소화'에서 백경은 은단오를 죽이고 왕이 되겠다 하고, 하루는 섀도우에서 단오에게 함께 도망가자고 한다."
        "백경은 하루가 단오 낭자를 좋아하고 있다는 것을 알게 된다. 단오 낭자는 결국 죽게 된다."

        scene kitchen
#
        "하루는 진미채에게 어떻게 된 것이냐 묻지만 진미채는 이야기는 반복되고 있으며 하루 너는 단오를 지킬 수 없으며 스테이지를 바꾸면 원치 않는 내용까지 바뀌게 되며 결국 비극적 결말을 볼 수밖에 없다고 말할 뿐이다."
        show jin at right
        jin "이야기가 틀어지면 보고싶지 않은것들을 보게 되고, 작가앞에 굴복하는 자신을 발견하게 돼"
        hide jin
        stop music
        play music "audio/Strange Feeling.mp3"
        scene stairs
#
        "스테이지. 단오의 수술 날짜가 잡힌다. 스테이지에서 단오는 백경에게 파혼의 이유를 설명해준다."

        show dano_sad at right
        dano "내가 왜 너랑 결혼하고 싶었는지 알아? 살고싶어서.. "
        dano "어렸을때 내 세상은 딱 2개였거든 병원 침대 세상과 백경 너 그래서 그랬나봐 그래서 너가 유일한 탈출구 같아 보였나봐 아팠던 심장이 나을 것 같고.. "
        dano "그래서 계속 좋아했나봐 너 감정따윈 상관 없이 너가 집안 일로 힘들어 하는거 알면서도.. 사람들은 너가 나한테 상처준다고 생각하겠지만 사실은 미안해 너한테 상처줘서."
        dano "그러니깐 우리 결혼 관두자 잘지내 백경아.."
        hide dano_sad

        "스테이지가 끝나고 단오는 백경에게 할말이 있다는 듯 말을 건다."

    elif(point8 == -1):
        stop music
        scene video
#
        "막으러 가려는 찰나 스테이지가 이미 시작되고 콘티대로 백경은 단오에게 프러포즈를 하게된다."

        show baek_happy at right
        baek "단오야 나랑 결혼해줄래?"
        hide baek_happy

        play music "audio/A Door To Time.mp3"
        scene classroom
        "단오는 자신이 수술을 받으며 사망하는 콘티를 본다."
        show dano_sad at right
        dano "내가.. 죽어..?"
        hide dano_sad
        stop music
        play music "audio/Ego.mp3"
        scene gung_2
        "하루는 '능소화'의 환상을 본다. 기억의 조각들이라 자세한 내용은 알긴 어렵다. '능소화'에서 백경은 은단오를 죽이고 왕이 되겠다 하고, 하루는 섀도우에서 단오에게 함께 도망가자고 한다."
        "백경은 하루가 단오 낭자를 좋아하고 있다는 것을 알게 된다. 단오 낭자는 결국 죽게 된다."

        scene kitchen
        "하루는 진미채에게 어떻게 된 것이냐 묻지만 진미채는 이야기는 반복되고 있으며 하루 너는 단오를 지킬 수 없으며 스테이지를 바꾸면 원치 않는 내용까지 바뀌게 되며 결국 비극적 결말을 볼 수밖에 없다고 말할 뿐이다."
        show jin at right
        jin "이야기가 틀어지면 보고싶지 않은것들을 보게 되고, 작가앞에 굴복하는 자신을 발견하게 돼"
        hide jin

        stop music
        play music "audio/Strange Feeling.mp3"
        scene stairs
        "스테이지. 단오의 수술 날짜가 잡힌다. 스테이지에서 단오는 백경에게 파혼의 이유를 설명해준다."

        show dano_sad at right
        dano "내가 왜 너랑 결혼하고 싶었는지 알아? 살고싶어서.. "
        dano "어렸을때 내 세상은 딱 2개였거든 병원 침대 세상과 백경 너 그래서 그랬나봐 그래서 너가 유일한 탈출구 같아 보였나봐 아팠던 심장이 나을 것 같고.. "
        dano "그래서 계속 좋아했나봐 너 감정따윈 상관 없이 너가 집안 일로 힘들어 하는거 알면서도.. 사람들은 너가 나한테 상처준다고 생각하겠지만 사실은 미안해 너한테 상처줘서."
        dano "그러니깐 우리 결혼 관두자 잘지내 백경아.."
        hide dano_sad

        "스테이지가 끝나고 단오는 백경에게 할말이 있다는 듯 말을 건다."

    #선택지 9번
    $ point9 = 0
    menu:
        "이제 시간이 얼마 안 남은 것 같으니 남은 시간만이라도 사이좋게 지내자고 한다": #하루
            $ point9 = point9 + 1

        "수술이 끝날 때까지 기다려 달라는 말을 한다": #백경
            $ point9 = point9 - 1

    if(point9 == 1):
#
        show dano_happy at right
        dano "나한테 정말 이제 시간이 얼마 안남았다는게 느껴져 스테이지에서는 설정값이니깐 어쩔수 없지만 남은시간동안 사이좋게 지내자"
        dano "다른 얘들한테 아무말 하지 말아줘"
        "다음날, 단오는 얼마 남지 않았지만 남은 시간이라도 하루와 도화가 걱정 없이 지낼 수 있도록 진미채에게 수술받는다는 사실을 말하지 말아 달라 신신당부한다."
        hide dano_happy
        stop music

        scene classroom
#
        "백경은 단오에게 지금까지는 사업상 지시된 정략결혼이 싫어서 단오를 밀어냈지만, 사실 마음은 너를 좋아하고 있었다며 단오에게 고백한다."

        show baek_happy at right
        baek "너 좋아하는거 이제 인정해 지금은 스테이지 아니야"
        hide baek_happy

        "하루는 옆에서 이 장면을 보게 되고 하루는 백경과 기싸움을 벌인다. 백경은 하루에게 정해진 대로 이야기가 흘러가고 있다고 말하고, 하루는 백경에게 그런 건 상관없다고 말한다."

        scene home

        "섀도우" " 백경은 단오의 집 앞으로 찾아가 다시 고백한다."


    elif(point9 == -1):
        stop music
        scene library
        "다음날, 단오는 얼마 남지 않았지만 남은 시간이라도 하루와 도화가 걱정 없이 지낼 수 있도록 진미채에게 수술받는다는 사실을 말하지 말아 달라 신신당부한다. "

        scene classroom
        "백경은 단오에게 지금까지는 사업상 지시된 정략결혼이 싫어서 단오를 밀어냈지만, 사실 마음은 너를 좋아하고 있었다며 단오에게 고백한다."
        show baek_happy at right
        baek "너 좋아하는거 이제 인정해 지금은 스테이지 아니야"
        hide baek_happy

        "하루는 옆에서 이 장면을 보게 되고 하루는 백경과 기싸움을 벌인다. 백경은 하루에게 정해진 대로 이야기가 흘러가고 있다고 말하고, 하루는 백경에게 그런 건 상관없다고 말한다."

        scene home
        "섀도우" " 백경은 단오의 집 앞으로 찾아가 다시 고백한다."

    #선택지 13번
    $ point10 = 0
    menu:
        "거절한다": #하루
            $ point10 = point10 + 1

        "수락한다": #백경
            $ point10 = point10 - 1

    if(point10 == 1):
        play music "audio/Take.mp3"
        scene home
#
        "자신이 백경을 좋아하는 것은 설정값일 뿐이고 진짜로는 좋아하지 않는 거 알지 않냐고 말하지만 백경은 섀도우가 진짜면 지금 자신이 단오를 좋아하는 건 그럼 진짜 아니냐고 화를 낸다."
        show baek at right
        baek "내가 소중하다고 생각한것들은 모두 떠났어 엄마처럼 그래서 안좋아 하고 싶었는데.."
        hide baek
        show dano_angry at right
        dano "미안한데 이러지마 \n"
        hide dano_angry
        show baek_angry at right
        baek "그럴꺼면 처음부터 나를 좋아하지 말았어야지"
        hide baek_angry
        show dano_angry at right
        dano "알잖아 그건 내 의지가 아니라 설정값이라는거"
        hide dano_angry
        show baek_angry at right
        baek "섀도우가 진짜라며 그럼 내가 널 좋아하는 마음도 진짜야"
        hide baek_angry
        show dano_angry at right
        dano "말했잖아 난 하루를 좋아한다고"
        hide dano_angry

        stop music
        scene classroom
        "한편 백경은 단오의 부탁이 무색하게 하루에게 단오가 수술받게 된다는 것을 말해버리고 하루는 단오가 다치거나 죽을까 봐 안절부절못한다."
        "백경은 이 각박한 만화 속 세상에서 지금까지 정신 줄 버티고 살 수 있었던 건 단오 너 덕이라며, 이야기는 바꿀 수 없으니 순리대로 수술받으면 살 수 있을 거라는 생각을 전한다. 하지만 하루는 죽는다는 콘티가 그대로 될까 봐 두려워한다."

        scene h_room
        "하루는 수술받는 이야기를 바꾸기 위해 도화의 형이자 단오의 주치의인 주화의 옷을 입고 주화의 방을 뒤진다. 하루는 그곳에서 단오의 차트가 담긴 파일을 열어 주화가 맡고 있는 다른 환자의 차트와 파일을 바꿔버린다."
        "스테이지는 바뀌어버리고 단오는 스테이지에서 수술을 받지 않아도 될 정도로 건강해졌다는 판정을 받는다."


        scene library

        "스테이지가 바뀌게 된 걸 알게 된 백경은 이야기를 바꾸려 하지 말라고 한다."
        "단오는 자신이 섀도우에서 자아를 가진 자신이 했던 말이 이미 '능소화'에서 했던 대사라는 것을 알고 자신이 의지대로 한 말들이 작가의 의지에 반한 모습이 맞는 것인지 혼란스러워한다."
        "한편, 하루는 건강해진 스테이지 속 설정값과 달리 섀도우에서 자꾸 심장병이 도지는 단오의 모습을 본다."

        "또한 주다의 할머니가 수술을 받게 된 날이 사실 단오가 수술받기로 한 날임을 알게 된 하루는 '능소화'에서 하루가 단오를 죽이는 모습을 봤다는 백경의 말에 단오가 수술받지 않도록 이야기를 바꾼 것이 잘못된 선택이 아닐까 걱정을 한다"
        "한편 단오는 스테이지에서 완치 판정을 받고, 백경의 진심 어린 프로포즈 까지 받는다. 하지만 섀도우로 돌아온 단오는 스테이지를 벗어나 이야기를 바꾸고만 싶어 하고, 스테이지와 설정값대로 단오와 결혼하고 싶은 백경은 그런 단오의 모습에 씁쓸해한다."

        scene gung_4
        play music "audio/Ego.mp3"
        "하루는 '능소화'의 환상을 본다. 백경은 진미채를 독살하려 하고 단오는 스테이지를 바꾸기 위해 독이 든 음식을 먹지 못하게 하려 하지만 진미채는 운명을 거스르려 하지 않겠다며 결국 음식을 씹어 삼킨다."

        scene gung_3
        "하루는 단오와 함께 스테이지 밖으로 도망가려 하지만 둘은 이내 스테이지로 소환된다. 백경은 반역죄를 씌워 단오를 죽이려 하고 하루는 이를 막으려 한다. 하지만 백경은 하루에게 직접 단오를 죽이라 명하고 하루는 자신이 원치 않게도 단오를 칼로 찌르게 된다."
        "이 장면을 떠올린 하루는 자신이 단오와 함께 있다간 단오를 죽이게 될지 모른다는 생각에 단오를 자꾸 피하게 되고, 영문을 모르는 단오는 당황하지만 결국 심장병은 도지고 급하게 병원으로 실려간다."

        scene hospital
        "입원실에서 산소호흡기를 끼고 있는 단오. 스테이지에선 건강한 설정이 있는 단오이기에 이곳은 섀도우가 분명하다. 백경은 누워있는 단오를 보며 차라리 수향처럼 자아를 잃는 편이 맘 편할지도 모르겠다는 진미채의 말을 떠올린다"
        "백경은 떨리는 손으로 다른 사람 몰래 단오의 산소호흡기를 떼버린다. 그 순간 '능소화'의 숨겨진 이야기가 나오게 되는데, 사실 능소화에서 단오를 찌른 것은 하루가 아니었다. 단오를 찌른 것은 백경이었고, "
        "하루는 그걸 막기 위해 백경의 칼을 잡은 것뿐이었던 것이다. 백경은 '능소화'에 이어 또다시 단오를 죽이게 된 결과가 되어버렸다.​"

#
        show baek at right
        baek "은단오.. (흐느끼면서 운다)"
        hide baek
        "단오의 상태가 되돌릴 수 없게 나빠진 다음 다시 산소호흡기를 걸고 입원실을 나오는 백경."
        "입원실로 들어가려는 하루와 마주친 백경은 하루에게 바꾸지 않으려 했는데, 그게 나라서 바꿀 수 없다는 알 수 없는 말을 한다. 단오는 결국 숨을 거두고 하루가 그 순간을 울며 지킨다"


        "단오가 숨을 거둔 그 순간 장면은 초기화된다. "

        scene classroom
        "하루는 스테이지 속 학교로 소환되고 하루의 눈앞에 단오가 나타난다. 하루는 기뻐하며 단오의 손을 잡지만, 모든 기억을 잃고 자아가 사라진 단오는 무심하게도 그 손을 뿌리친다. "
        show haru_sad at right
        haru "단오야 잠깐만.. 잠깐만 나랑 얘기좀 해"
        hide haru_sad
        "학교로 소환된 하루는 멀쩡한 모습으로 걸어오는 단오의 손을 덥석 잡지만 자아가 사라진 단오는 하루의 손을 뿌리친다."
        show dano_happy at right
        dano "백경아 아무리 생각해도 이건 사랑의 힘 같아 아니면 이 기적을 어떻게 설명하겠어"
        "백경은 자신에게 다정한 모습을 보이는 단오의 모습에 당황을 넘어 당혹해한다. "
        hide dano_happy

#
        "하루는 백경에게 어찌 된 일이냐 묻지만 원래 날이 서있는 백경은 모든 게 제자리로 돌아간 것 아니겠느냐는 반응을 보인다."
        "하지만 백경은 단오를 죽이던 능소화 속 자신의 모습을 떠올리며 단오의 산소호흡기를 벗겼던 자신의 모습에 복잡한 감정을 느낀다. "

        scene kitchen
#
        "하루는 진미채를 찾아와 영문을 묻는다."
        show haru_sad at right
        haru "단오가 기억이 사라졌어요.. "
        hide haru_sad
        show jin at right
        jin "널 보면 예전에 내가 생각나 딱 그 표정이었어 내가 그 아이를 잃었을때"
        hide jin

        "진미채는 섀도우에서 죽으면 자아를 잃고, 작품이 끝나면 캐릭터들은 다른 작품에서 그려질 때까지 깊은 잠에 빠져버린다는 만화 속 세계의 법칙을 설명해준다"
        "또한 이야기가 끝나갈 때쯤이면 작가가 작품을 정리하기 위해 비중이 작은 엑스트라부터 지워가니 작가 눈에 띄지 않게 조심하라 말한다."
#
        show jin at right
        jin "이제 몇장면 안남았잖아 작가가 이 세계를 정리하는 일만 남았어 "
        hide jin

        scene classroom

        "같은 반에 있었던 보통이가 사라진 걸 알게 되자 이 세상이 얼마 남지 않았다는 걸 직감하게 된다."
        "하루는 이야기가 계속 이어지던 만화책 '비밀'의 백지 부분이 몇 장 남지 않았으며, 하루는 백경에게 능소화 속 단오를 죽인 게 내가 아니라 너 아니냐고 다그친다. "
        "능소화에서도 비밀에서도 너 때문에 힘든 단오의 자아를 내가 찾아주겠다고 선언한다. 하루는 자신이 자아를 잃었을 때 단오가 기억을 찾아주기 위해 했었던 행동들을 단오에게 따라 하며 쫓아다닌다."
        "단오는 자기반 학생일 뿐인 하루가 계속 자기에게 엉겨 붙는 모습에 당황해한다. 하지만 하루가 다가올 때마다 언뜻언뜻 떠오르는 설렌 기억으로 인해 심박수가 올라가 스마트워치까지 경보음을 울리자 혼란함을 느낀다."

        stop music
        scene stairs
        "자아를 잃고 자신의 설정값대로 백경을 좋아하고 있는 단오는 백경과 난생처음 데이트를 한다. 하지만 백경은 지금 보여주는 단오의 모습이 그저 설정값에 따른 것이지 진짜 단오의 모습이 아니라는 사실에 씁쓸해한다."
        "비록 가짜더라도 자신을 좋아하는 단오의 모습을 보길 바랐던 백경은 정작 단오를 보니 죄책감을 느끼며 자신을 괴물이라 자책하게 된다."
        "백경은 무언가 결심한 듯 단오와 다음 데이트 약속을 잡는다. "

        scene library

#
        show baek at right
        baek "곧있으면 은단오랑 내 스테이지가 시작될꺼야 나대신 니가 가던지 착각하지마 널 도와줄 마음은 없고 은단오 소원은 아마 너.. 아니 빌어먹을 작가가 싫어서 이러는거니깐"
        "약속을 잡은 백경은 하루에게 자신의 외투를 빌려주며 단오를 위해 스테이지를 바꿔달라고 요청한다. "
        hide baek

        play music "audio/Strange Feeling.mp3"

        scene tree
        "곧이어 시작된 스테이지. 하루는 아름드리나무 앞에서 백경의 외투를 입은 채 등을 돌려 서있다."
        "단오는 뒤돌아 서있던 하루에게 살금살금 다가가 하루의 등에 자신의 등을 맞댄다. 단오는 순간 자아를 가지고 있던 지난날이 모두 떠오르면서 '능소화' 속 기억까지 모두 되찾게 된다."
        "자아를 찾은 단오는 자아를 찾은 기쁨과 하루에 대한 미안함을 가지고 있다"

    elif(point10 == -1):
        play music "audio/Strange Feeling.mp3"
#
        scene home
        show baek at right
        baek "수술 받아 그럼 살 수 있을거야"
        hide baek
        "백경은 이 각박한 만화 속 세상에서 지금까지 정신 줄 버티고 살 수 있었던 건 단오 너 덕이라며, 이야기는 바꿀 수 없으니 순리대로 수술받으면 살 수 있을 거라는 생각을 전한다."

        stop music
        scene classroom
        "한편 백경은 하루에게 단오가 수술받게 된다는 것을 말해버리고 하루는 단오가 다치거나 죽을까 봐 안절부절못한다."

        scene h_room
        "하루는 수술받는 이야기를 바꾸기 위해 도화의 형이자 단오의 주치의인 주화의 옷을 입고 주화의 방을 뒤진다. 하루는 그곳에서 단오의 차트가 담긴 파일을 열어 주화가 맡고 있는 다른 환자의 차트와 파일을 바꿔버린다."
        "스테이지는 바뀌어버리고 단오는 스테이지에서 수술을 받지 않아도 될 정도로 건강해졌다는 판정을 받는다. "

        scene library
        "스테이지가 바뀌게 된 걸 알게 된 백경은 이야기를 바꾸려 하지 말라며 능소화를 보여주고"
        "단오는 자신이 섀도우에서 자아를 가진 자신이 했던 말이 이미 '능소화'에서 했던 대사라는 것을 알고 자신이 의지대로 한 말들이 작가의 의지에 반한 모습이 맞는 것인지 혼란스러워한다."
        "한편, 하루는 건강해진 스테이지 속 설정값과 달리 섀도우에서 자꾸 심장병이 도지는 단오의 모습을 본다."
        "또한 주다의 할머니가 수술을 받게 된 날이 사실 단오가 수술받기로 한 날임을 알게 된 하루는 '능소화'에서 하루가 단오를 죽이는 모습을 봤다는 백경의 말에 단오가 수술받지 않도록 이야기를 바꾼 것이 잘못된 선택이 아닐까 걱정을 한다"
        "한편 단오는 스테이지에서 완치 판정을 받고, 백경의 진심 어린 프로포즈 까지 받는다."

        play music "audio/Ego.mp3"
        scene gung_4
        "하루는 '능소화'의 환상을 본다. 백경은 진미채를 독살하려 하고 단오는 스테이지를 바꾸기 위해 독이 든 음식을 먹지 못하게 하려 하지만 진미채는 운명을 거스르려 하지 않겠다며 결국 음식을 씹어 삼킨다."

        scene gung_3
        "하루는 단오와 함께 스테이지 밖으로 도망가려 하지만 둘은 이내 스테이지로 소환된다. 백경은 반역죄를 씌워 단오를 죽이려 하고 하루는 이를 막으려 한다. 하지만 백경은 하루에게 직접 단오를 죽이라 명하고 하루는 자신이 원치 않게도 단오를 칼로 찌르게 된다."
        "이 장면을 떠올린 하루는 자신이 단오와 함께 있다간 단오를 죽이게 될지 모른다는 생각에 단오를 자꾸 피하게 되고, 영문을 모르는 단오는 당황하지만 결국 심장병은 도지고 급하게 병원으로 실려간다."

        scene hospital
        "입원실에서 산소호흡기를 끼고 있는 단오. 스테이지에선 건강한 설정이 있는 단오이기에 이곳은 섀도우가 분명하다. 백경은 누워있는 단오를 보며 차라리 수향처럼 자아를 잃는 편이 맘 편할지도 모르겠다는 진미채의 말을 떠올린다"
        show baek at right
        baek "은단오.. (흐느끼면서 운다)"
        hide baek

        "백경은 떨리는 손으로 다른 사람 몰래 단오의 산소호흡기를 떼버린다. 그 순간 '능소화'의 숨겨진 이야기가 나오게 되는데, 사실 능소화에서 단오를 찌른 것은 하루가 아니었다. 단오를 찌른 것은 백경이었고,"
        "하루는 그걸 막기 위해 백경의 칼을 잡은 것뿐이었던 것이다. 백경은 '능소화'에 이어 또다시 단오를 죽이게 된 결과가 되어버렸다.​"
        "단오의 상태가 되돌릴 수 없게 나빠진 다음 다시 산소호흡기를 걸고 입원실을 나오는 백경. 입원실로 들어가려는 하루와 마주친 백경은 하루에게 바꾸지 않으려 했는데, 그게 나라서 바꿀 수 없다는 알 수 없는 말을 한다. 단오는 결국 숨을 거두고 하루가 그 순간을 울며 지킨다"
        "단오가 숨을 거둔 그 순간 장면은 초기화된다. 하루는 스테이지 속 학교로 소환되고 하루의 눈앞에 단오가 나타난다. 하루는 기뻐하며 단오의 손을 잡지만, 모든 기억을 잃고 자아가 사라진 단오는 무심하게도 그 손을 뿌리친다. "

        scene classroom
        "학교로 소환된 하루는 멀쩡한 모습으로 걸어오는 단오의 손을 덥석 잡지만 자아가 사라진 단오는 하루의 손을 뿌리친다. 백경은 자신에게 다정한 모습을 보이는 단오의 모습에 당황을 넘어 당혹해한다. "
        "하루는 백경에게 어찌 된 일이냐 묻지만 원래 날이 서있는 백경은 모든 게 제자리로 돌아간 것 아니겠느냐는 반응을 보인다. 하지만 백경은 단오를 죽이던 능소화 속 자신의 모습을 떠올리며 단오의 산소호흡기를 벗겼던 자신의 모습에 복잡한 감정을 느낀다. "

        scene kitchen
        "하루는 진미채를 찾아와 영문을 묻는다. "
        show haru_sad at right
        haru "단오가 기억이 사라졌어요.. "
        hide haru_sad
        show jin at right
        jin "널 보면 예전에 내가 생각나 딱 그 표정이었어 내가 그 아이를 잃었을때"
        hide jin

        "진미채는 섀도우에서 죽으면 자아를 잃고, 작품이 끝나면 캐릭터들은 다른 작품에서 그려질 때까지 깊은 잠에 빠져버린다는 만화 속 세계의 법칙을 설명해준다"
        "또한 이야기가 끝나갈 때쯤이면 작가가 작품을 정리하기 위해 비중이 작은 엑스트라부터 지워가니 작가 눈에 띄지 않게 조심하라 말한다."

        show jin at right
        jin "이제 몇장면 안남았잖아 작가가 이 세계를 정리하는 일만 남았어 "
        hide jin

        scene classroom
        "하루는 이야기가 계속 이어지던 만화책 '비밀'의 백지 부분이 몇 장 남지 않았으며, 하루는 백경에게 능소화 속 단오를 죽인 게 내가 아니라 너 아니냐고 다그친다."
        "능소화에서도 비밀에서도 너 때문에 힘든 단오의 자아를 내가 찾아주겠다고 선언한다. 하루는 자신이 자아를 잃었을 때 단오가 기억을 찾아주기 위해 했었던 행동들을 단오에게 따라 하며 쫓아다닌다."
        "단오는 자기반 학생일 뿐인 하루가 계속 자기에게 엉겨 붙는 모습에 당황해한다. 하지만 하루가 다가올 때마다 언뜻언뜻 떠오르는 기억으로 혼란함을 느낀다."

        stop music
        scene stairs
        "자아를 잃고 자신의 설정값대로 백경을 좋아하고 있는 단오는 백경과 난생처음 데이트를 한다. 하지만 백경은 지금 보여주는 단오의 모습이 그저 설정값에 따른 것이지 진짜 단오의 모습이 아니라는 사실에 씁쓸해한다."
        "비록 가짜더라도 자신을 좋아하는 단오의 모습을 보길 바랐던 백경은 정작 단오를 보니 죄책감을 느끼며 자신을 괴물이라 자책하게 된다."
        "백경은 무언가 결심한 듯 단오와 다음 데이트 약속을 잡는다. "


        play music "audio/Strange Feeling.mp3"
        scene tree
        "곧이어 시작된 스테이지. 백경은 아름드리나무 앞에서 등을 돌려 서있다."
        "단오는 뒤돌아 서있던 백경에게 살금살금 다가가 백경의 등에 자신의 등을 맞댄다. 단오는 순간 자아를 가지고 있던 지난날이 모두 떠오르면서 '능소화' 속 기억까지 모두 되찾게 된다."
        "자아를 찾은 단오는 자아를 찾은 기쁨과 백경에 대한 미안함을 가지고 있다"

    #선택지 14번
    $ point11 = 0
    menu:
        "단오는 하루를 울며 껴안는다.": #하루
            $ point11 = point11 + 1
        "단오는 벽경을 껴안는다": #백경
            $ point11 = point11 - 1

    if(point11 == 1):

        scene tree
        "자아를 찾은 단오는 자아를 찾은 기쁨과 하루에 대한 미안함으로 울며 하루를 껴안는다."

        scene classroom
#
        "백경은 자아를 찾은 단오의 얼굴을 보기 미안한지 수업도 들어가지 않고 숨어있듯 학교 안 아지트에 앉아있다."
        "단오는 백경을 찾아간다. 미안해서 어쩔 줄 모르는 백경에게 위로의 말을 건넨다."

        show dano at right
        dano "백경아.. (반지를 건내준다)"
        hide dano

        show baek at right
        baek "가.. 가라고 그떄도 지금도 나는 너한테 괴물같아"
        hide baek

        show dano at right
        dano "적어도 순정만화 비밀의 은단오한테 넌 그런사람 아니야"
        "비밀의 은단오로서 시한부 설정값에 해방되게 해 주서 고마웠고, 능소화의 은단오로서 설정값 때문에 자신을 죽인 걸 이해하고 용서한다고 말한다. 자신이 자아를 찾고 진짜 은단오가 될 수 있었던 것처럼 백경 너도 싸가지 설정값의 백경이 아니라 진짜 백경을 찾기 바란다는 말을 남긴다."
        hide dano


        stop music
        play music "audio/Ego.mp3"
        scene library
        "하루의 명찰에서 '하루'라는 이름이 사라진다. 단오가 '하루'라는 이름을 지어주면서 이름이 생긴 명찰이다. 그 명찰에서 이름이 사라진다는 것은 하루도 보통이처럼 곧 사라진다는 걸 의미한다는 걸 하루도 잘 알고 있다."
        "하루는 단오가 그 명찰을 보게 될까 봐 단오를 꼭 껴안는다. "

        stop music
        play music "audio/Solitude.mp3"
        scene art
        "단오는 하루가 커터 칼로 담요에 구멍을 뚫어 별을 보여준 추억이 어린 미술실에서 데이트를 즐긴다. 단오는 하루에게 우리가 '비밀'의 마지막 페이지까지 항상 함께 있자고 말한다. "

        stop music
        play music "audio/Burning Light.mp3"
        scene s_load
        "미술실에서 나온 하루와 단오. 하루는 미술실에서 이상한 소리가 들리자 문을 열어보는데 미술실은 마치 우주를 보는 것처럼 암흑에 빠져있다."
        "미술실에 있던 이젤, 석고상 등이 떠다니다가 사라진다. 작가가 불필요한 공간부터 정리하고 있던 것이다. 하루는 단오가 미술실을 열어보지 못하게 얼른 닫아버린다."

        show dano at right
        dano "무슨일이야\? 다시 가보자"
        hide dano

        show haru at right
        haru "별거 아니야 그냥 섀도우에서 있는 흔한 일일꺼야"
        hide haru

        scene classroom
        "하루는 교실로 급하게 돌아와 출석표를 보는데. 출석표에는 보통이는 물론 자신의 얼굴조차 사라져 있자 마지막을 준비한다. 하루는 우연히 단오의 버킷리스트를 보게 된다."

        stop music
        play music "audio/Solitude.mp3"
        scene library
        "단오의 버킷리스트에는 편지 쓰기, 커플 템 맞추기, 뽀뽀하기 등이 쓰여있다. 하루는 단오의 책상에 편지도 써주고 색종이로 커플 목걸이를 만들어 선물해준다. 단오에게 뽀뽀도 한다."

        stop music
        play music "audio/Burning Light.mp3"
        "하지만 하루는 자꾸 단오의 눈앞에서 사라지게 된다. 단오는 학교를 뒤져 도서실로 소환된 하루를 찾는다. 하지만 이내 도서관이 어두워진다. 도서관이라는 공간도 정리되고 있다는 뜻이다"

        scene s_load_2
        "하루는 자신이 사라지는 공간과 함께 소멸되는 것을 피하기 위해 단오의 손을 잡고 뒤에서 쫓아오는 어둠을 피해 학교 로비로 뛰어나온다. 하지만 하루는 곧 자신이 사라질 운명이고 이를 거스를 수 없다는 걸 알고 있다. "
        "하루는 단오에게 마지막 인사를 건넨다. 이내 어둠은 하루를 집어삼킨다"

    elif(point11 == -1):

        scene tree
        "백경은 자아를 찾은 단오의 얼굴을 보기 미안해하고 단오는 어쩔 줄 모르는 백경에게 위로의 말을 건넨다."
        "비밀의 은단오로서 시한부 설정값에 해방되게 해 주서 고마웠고, 능소화의 은단오로서 설정값 때문에 자신을 죽인 걸 이해하고 용서한다고 말한다. 자신이 자아를 찾고 진짜 은단오가 될 수 있었던 것처럼 백경 너도 진짜 백경을 찾기 바란다는 말을 남긴다."

        stop music
        play music "audio/Ego.mp3"
        scene library
        "하루의 명찰에서 '하루'라는 이름이 사라진다. 단오가 '하루'라는 이름을 지어주면서 이름이 생긴 명찰이다. 그 명찰에서 이름이 사라진다는 것은 하루도 보통이처럼 곧 사라진다는 걸 의미한다는 걸 하루도 잘 알고 있다."
        "하루는 단오가 그 명찰을 보게 될까 봐 이름표를 가린다. "

        stop music
        play music "audio/Solitude.mp3"
        scene art
        "단오는 백경은 미술실에서 데이트를 즐긴다. 단오는 백경에게 우리가 '비밀'의 마지막 페이지까지 항상 함께 있자고 말한다. "

        stop music
        play music "audio/Burning Light.mp3"
        scene s_load
        "미술실에서 나온 백경과 단오. 백경은 미술실에서 이상한 소리가 들리자 문을 열어보는데 미술실은 마치 우주를 보는 것처럼 암흑에 빠져있다."
        "미술실에 있던 이젤, 석고상 등이 떠다니다가 사라진다. 작가가 불필요한 공간부터 정리하고 있던 것이다. 백경은 단오가 미술실을 열어보지 못하게 얼른 닫아버린다."

        show dano at right
        dano "무슨일이야\? 다시 가보자"
        hide dano

        show baek at right
        baek "별거 아니야 그냥 섀도우에서 있는 흔한 일일꺼야"
        hide baek

        scene library
        "하루는 자꾸 사라지게 된다. 단오는 학교를 뒤져 도서실로 소환된 하루를 찾는다. 하지만 이내 도서관이 어두워진다. 도서관이라는 공간도 정리되고 있다는 뜻이다"

        scene s_load_2
        "하루는 자신이 사라지는 공간과 함께 소멸되는 것을 피하기 위해 단오와 뒤에서 쫓아오는 어둠을 피해 학교 로비로 뛰어나온다. 하지만 하루는 곧 자신이 사라질 운명이고 이를 거스를 수 없다는 걸 알고 있다. "

    #선택지 15번
    $ point12 = 0
    menu:
        "학교 건물 밖으로 나간다": #하루
            $ point12 = point12 + 1

        "마지막 인사를 건넨다": #백경
            $ point12 = point12 - 1

    if(point12 == 1):
        stop music
        scene tree
        "다음 스테이지에 나올 공간이기 때문에 사라지지 않는다."
        scene end
        "단오와 하루는 스테이지로 소환된다. 이번 스테이지는 시간이 껑충 뛴 1년 뒤의 스리고 졸업식이다. 비밀의 백지는 이제 한 장만이 남아있을 뿐이다."
        "졸업식엔 주다를 괴롭히던 양아치들이 서열 1위의 여자인 서열 0위 주다에 게 혼나는 모습, 영상제에서 고백해 결혼까지 성공한 양일과 일진이 사랑을 이어가는 모습 등이 그려진다."
        "단오는 같은 반 친구들과 단체사진도 찍는다. 그 순간, 만화 '비밀'이 끝나고 화면은 암전 된다"

        play music "audio/어쩌다 심쿵 코믹.mp3"
        scene university
        "새로운 만화가 시작되고 새 이야기 속 캐릭터들의 모습이 보인다. 단오는 대학생이 되어 철학 수업을 듣고 있다. '비밀'에서 이름조차 소개되지 않았던 단역들이 새로운 이야기 속에선 주요인물이 되어 대학생활을 하는 모습들이 나오게 된다."
        "단오는 등장인물로도 나오지 못했던 '비밀' 속 하루의 모습처럼 이름표도 없는 사물함을 쓰고 있다."
        "단오는 공강시간을 이용해서 학교를 둘러볼 장소를 고민한다."

    elif(point12 == -1):
        stop music
        play music "audio/Strange Feeling.mp3"
        scene s_load_2
        show haru_sad at right
        haru "단오야.."
        hide haru_sad

        show dano_sad at right
        dano "안돼 널 지켜야해 안돼 사라지면 안돼"
        hide dano_sad

        show haru_sad at right
        haru "단오야 그떄는 지키지 못했지만 이번에는 네 운명이 달라져서 다행이다.. 미안해.. 마지막 장면에 같이 있어주지 못해서 단오야.. 울지마"
        haru "내 시작도 내 마지막도 너여서.. 내 이름 불러줘 단오야 내 이름.."
        hide haru_sad

        show dano_sad at right
        dano "하루 ... 하루야 ㅠㅠㅠ"
        hide dano_sad

        "이내 어둠은 하루를 집어삼키고, 단오의 눈앞에 있던 하루는 이내 먼지가 되듯 소멸해 버린다. 하루가 사라지는 모습을 본 단오는 슬퍼한다."

        stop music
        scene end
        "단오와 백경은 스테이지로 소환된다. 이번 스테이지는 시간이 껑충 뛴 1년 뒤의 스리고 졸업식이다. 비밀의 백지는 이제 한 장만이 남아있을 뿐이다."
        "졸업식엔 주다를 괴롭히던 양아치들이 서열 1위의 여자인 서열 0위 주다에 게 혼나는 모습, 영상제에서 고백해 결혼까지 성공한 양일과 일진이 사랑을 이어가는 모습 등이 그려진다."
        "단오는 같은 반 친구들과 단체사진도 찍는다. 그 순간, 만화 '비밀'이 끝나고 화면은 암전 된다"

        play music "audio/어쩌다 심쿵 코믹.mp3"
        scene university
        "새로운 만화가 시작되고 새 이야기 속 캐릭터들의 모습이 보인다. 단오는 대학생이 되어 철학 수업을 듣고 있다. '비밀'에서 이름조차 소개되지 않았던 단역들이 새로운 이야기 속에선 주요인물이 되어 대학생활을 하는 모습들이 나오게 된다."
        "단오는 등장인물로도 나오지 못했던 '비밀' 속 하루의 모습처럼 이름표도 없는 사물함을 쓰고 있다."
        "단오는 공강시간을 이용해서 학교를 둘러볼 장소를 고민한다."

    #선택지 16번
    $ point13 = 0
    menu:
        "하루와 추억이 있는 미술동아리 전시회로 간다.": #하루
            $ point13 = point13 + 1

        "백경과 추억이 있는 테니스장으로 간다": #백경
            $ point13 = point13 - 1

    if(point13 == 1):

        scene artshow
        "미술동아리 학생들의 미술작품들이 줄줄이 걸려있다. 단오는 그 그림 들 중 익숙한 그림을 보게 된다. 그 그림은 하루의 스케치 수첩에서 봤던 그림인 것이다."
        "그 그림에 놀란 단오는 그 그림을 그린 사람의 이름표를 보지만 그 이름표에는 아무 이름도 쓰여있지 않았다.​"
        "단오는 그림을 보자마자 학교를 이곳저곳 찾아다니는데, 오늘이 10월 10일인 것을 알게 되자 '비밀'에도 있었던 아름드리나무를 찾아간다."

        stop music
        play music "audio/Strange Feeling.mp3"

        scene tree_2
        "그곳에선 '비밀'에서의 약속을 지키려는 듯 하루가 서있었다."

        show dano_sad at right
        dano "찾았다.. 하루야!  "
        hide dano_sad

        "둘은 그곳에서 뜨겁게 포옹한다"

        show haru_sad at right
        haru "은단오... 보고 싶었어"
        hide haru_sad

        show dano_sad at right
        "보고 싶었어 하루야"
        hide dano_sad

    elif(point13 == -1):

        stop music
        play music "audio/Strange Feeling.mp3"
        scene tennis
        "테니스장에서 테니스를 치고 있는 백경을 발견하게 된다"
        "그 순간 비밀에서 테니스를 치던 백경의 모습이 떠오르고 기억을 찾게 된다."

        "둘은 그곳에서 뜨겁게 포옹한다. "

        show dano_sad at right
        dano "찾았다.. 백경아! 오래걸렸지.."
        hide dano_sad

        show baek at right
        baek "은단오... 보고 싶었어"
        hide baek

        show dano_sad at right
        dano "보고 싶었어 백경아"
        hide dano_sad

    return
