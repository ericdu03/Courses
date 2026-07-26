(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr(cdr s))))

(define (ordered? s) 
    (cond
        ((null? s) #t)
        ((null? (cdr s)) #t)
        ((< (car s) (cadr s)) (ordered? (cdr s)))
        ((> (car s) (cadr s)) #f)
        (else (ordered? (cdr s)))
    )
)



(define (square x) (* x x))

(define (pow base exp) 
    (cond
        ((= exp 1) base)
        ((= exp 2) (square base))
        ((= (remainder exp 2) 0 ) square (pow base (/ exp 2)))
        (else (* base (square (pow base (/ (- exp 1) 2)))  )  )
    
    )
    


)