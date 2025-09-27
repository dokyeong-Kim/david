# ia-codyssey
Github와 codyssey을 연동하기 위해 만들어진 Repository

## 반달곰 커피 홈페이지
[참조링크] https://반달곰커피

오디오 출력 소스코드
```
lang = request.args.get('lang', DEFAULT_LANG)
fp = BytesIO()
gTTS(text, "com", lang).write_to_fp(fp)
encoded_audio_data = base64.b64encode(fp.getvalue())
```
![안보임](pre-learn/7/david/static/david.jpg)


