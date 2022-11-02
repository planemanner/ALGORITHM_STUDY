# Pollard Rho Algorithm
  - [Reference](https://nyan101.github.io/blog/algorithms-for-integer-factorization)
  - pollard-rho(ρ) 알고리즘은 일종의 충돌쌍을 이용해 소인수를 찾는 방식
  - 구체적으로, 어떤 x,x′이 x≠x′, x≡x′(modp)을 만족한다면 gcd(x−x′,n) 은 최소한 p를 약수로 가진다는 사실을 이용한다
  - 랜덤한 a,b들을 시험해보면서 gcd(a−b,n)>1 을 만족하는지 알아보는 대신, 조사를 효율적으로 진행하기 위해 변환규칙을 사용한다.
