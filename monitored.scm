(define (make-monitored f)
  (let ((count 0))
    (define (dispatch m)
       (if (eq? m 'how-many-calls?)
           count
           (begin (set! count (+ count 1))
                  (f m))))
    dispatch))
(define s (make-monitored sqrt))
(s 100)
(s 'how-many-calls?)
(s 1000)
(s 'how-many-calls?)


