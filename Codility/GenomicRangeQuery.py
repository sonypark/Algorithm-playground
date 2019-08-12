
def genomicRangeQuery(S,P,Q):
    nucleotide = [0]*len(S)

    for i in range(len(S)):
        if S[i] =='A': nucleotide[i] = 1
        elif S[i] =='C': nucleotide[i] = 2
        elif S[i] =='G': nucleotide[i] = 3
        else: nucleotide[i] = 4

    z = zip(P,Q)
    answer =[]

    for s,e in z:
        answer.append(min(nucleotide[s:e+1]))
    return answer

s ='CAGCCTA'
p = [2,5,0]
q = [4,5,6]
print(genomicRangeQuery(s,p,q))


## 다른 사람 풀이
def solution(S, P, Q):
    cost_dict = {'A':1, 'C':2, 'G':3, 'T':4}

    curr_counts = [0,0,0,0]
    counts = [curr_counts[:]]
    for s in S:
        curr_counts[cost_dict[s]-1] += 1
        counts.append(curr_counts[:])

    results = []
    for i in range(len(Q)):
        counts_q = counts[Q[i] + 1]
        counts_p = counts[P[i]]

        if Q[i] == P[i]:
            results.append(cost_dict[S[Q[i]]])
        elif counts_q[0] > counts_p[0]:
            results.append(1)
        elif counts_q[1] > counts_p[1]:
            results.append(2)
        elif counts_q[2] > counts_p[2]:
            results.append(3)
        elif counts_q[3] > counts_p[3]:
            results.append(4)

    return results



'''
# 시간 초과
def genomicRangeQuery(S,P,Q):
    nucleotide = [0]*len(S)

    for i in range(len(S)):
        if S[i] =='A': nucleotide[i] = 1
        elif S[i] =='C': nucleotide[i] = 2
        elif S[i] =='G': nucleotide[i] = 3
        else: nucleotide[i] = 4

    z = zip(P,Q)
    answer =[]
    for s,e in z:
        answer.append(min(nucleotide[s:e+1]))
    return answer
'''