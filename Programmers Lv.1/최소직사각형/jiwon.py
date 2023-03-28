def solution(sizes):
    answer = 0
    w_max=0
    h_max=0
    for i in sizes:
        if(i[0]<i[1]):
            i[0],i[1] = i[1],i[0]
        if(w_max<i[0]):
            w_max=i[0]
        if(h_max<i[1]):
            h_max=i[1]
    return w_max*h_max

# for a,b in sizes -> 요소가 두개일때 a,b로 꺼내기 가능
# max(w_max,i[0])으로 구하기 가능. max() 함수 이용
# sum(list,[])를 통해 2차원 리스트를 1차원으로 만들수 있다.
# lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)