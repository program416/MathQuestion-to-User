# .dta 파일 문법
**DTA는 886바이트 초경량 언어 입니다.**
## 주석
주석은 다음과 같이 만들 수 있습니다.
**comment.dta**
```dta
#config start;
# -j # 이것이 바로 주석입니다.;
# -j # #config start와 #config end는 꼭 필요합니다.;
#config end;
```

## 출력
출력은 다음과 같이 할 수 있습니다.
**print.dta**
```dta
#config start;
# -j # 밑 문장은 문자열을 출력합니다./je
prt(안녕하세요);
# -j # 세미콜론은 꼭 붙여야 하며 괄호 안 들어간 것이 출력됩니다./je
#config end;
```

## 이스터 에그
이스터 에그는 이것입니다
```dta중일부
esteg.view();
```