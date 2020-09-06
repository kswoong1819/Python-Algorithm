def solution(word, pages):
    L = len(pages)
    point = [0] * L
    ex_point = [0] * L
    link = [0] * L
    for i in range(L):
        st = pages[i].index("<body>")
        ed = pages[i].index("</body>")
        cnt = pages[i].lower().count(word.lower(), st, ed)
        for k in range(cnt):
            idx = pages[i].lower().index(word.lower(), st, ed)
            st = idx + 1
            if pages[i][idx - 1].isalpha() or pages[i][idx + len(word)].isalpha():
                continue
            else:
                point[i] += 1

        idx2 = pages[i].index("content")
        check = idx2 + 17
        while 1:
            if pages[i][check] == '\"':
                break
            else:
                check += 1
        in_link = pages[i][idx2 + 17:check]
        link[i] = in_link

    for i in range(L):
        st = pages[i].index("<body>")
        ed = pages[i].index("</body>")
        cnt2 = pages[i].count("a href")
        st2 = st
        for k2 in range(cnt2):
            idx3 = pages[i].index("a href", st2, ed)
            st2 = idx3 + 16
            while 1:
                if pages[i][st2] == '\"':
                    break
                else:
                    st2 += 1
            ex_link = pages[i][idx3 + 16:st2]
            for t in range(len(link)):
                if link[t] == ex_link:
                    ex_point[t] += point[i] / cnt2
                    break

    answer = 0
    max_point = 0
    for i in range(len(point)):
        total = point[i] + ex_point[i]
        if max_point < total:
            max_point = total
            answer = i

    print(link)
    print(point)
    print(ex_point)
    return answer


w = "blind"
p = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a\"/>\n</head>  \n<body>\n<a href=\"https://b\"> Link to b </a>\nblind Lorem blInd ipsum dolor blind test sit amet, consectetur adipiscing elit. \n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a\"> Link to a </a>\n</body>\n</html>"
]

# w = "Muzi"
# p = [
#     "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
#     "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"
# ]
print(solution(w, p))
