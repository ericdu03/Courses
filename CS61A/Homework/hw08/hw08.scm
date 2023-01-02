(define (my-filter func lst)
  (if (null? lst) '() 
    (if (func (car lst)) (append (list (car lst)) (my-filter func (cdr lst)))
      (my-filter func (cdr lst))
    )
  )
)

(define (interleave s1 s2) 
  (if (null? s1) s2
    (if (null? s2) s1
      (append (list (car s1)) (list (car s2)) (interleave (cdr s1) (cdr s2)))
    )
  )
)

(define (accumulate merger start n term)
  (if (= n 0) start
    (merger (term n) (accumulate merger start (- n 1) term))
  )
)

(define (no-repeats lst)
  (if (null? lst) '()
    (cons (car lst) (my-filter (lambda (x) (not (= x (car lst)))) (no-repeats (cdr lst)) ))
  )
)


