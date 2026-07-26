(define (over-or-under num1 num2)
    ;(if (= num1 num2) 0
    ;(if (> num1 num2) 1 -1))
    (cond ((> num1 num2) 1) ((= num1 num2) 0) ((< num1 num2) -1 ))
)
    
(define (make-adder num) 
    (lambda (inc) (+ num inc))
)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

(define lst 
    ;(list (list 1) 2 (list 3 4) 5)
    (cons 
        (cons 1 nil ) 
        (cons 2 
            (cons (cons 3 (cons 4 nil )) (cons 5 nil ))
        ) 
    )  
)

(define (remove item lst) 
    (if (= lst nil ) nil 
        (if (= (cdr lst) nil ) lst
            (filter (= item (car lst)) (lst))))

    (remove item (cdr lst))
)
