(defclass rat
  :super propertied-object ;;親クラス
  :slots (numer denom) ;;スロットリスト
  )
(defmethod rat
  (:init (n d)
	 (setq numer n)
	 (setq denom d)
	 self) ;;初期化
  (:denom () denom)
  (:numer () numer)
  (:add (y)
	(instance rat :init(+(* numer (send y :denom))
			     ( * (send y :numer) denom))
		  (* denom (send y :denom))))
  (:sub (y)
        (instance rat :init(- (* (send y :numer) denom)
			      (* numer (send y :denom)))
                  (* denom (send y :denom))))
  (:mul (y)
	(instance rat :init(* numer (send y :numer))
		  (* denom (send y :denom))))
  (:div (y)
	(instance rat :init(* denom (send y :numer))
		  (* numer (send y :denom))))



			    
  (:prin1 (strm) (format strm "~A/~A" numer denom))
  )

(defun make-rat (n d)
    (instance rat :init n d))


;;denom Bunbo
;;numer Bunshi

(setq one-half (make-rat 1 2))
(print one-half)
(setq one-third (make-rat 1 3))
(print one-third)
(format t "add")
(print (send one-third :add one-half))
(format t "sub")
(print (send one-third :sub one-half))
(format t "mul")
(print (send one-third :mul one-half))
(format t "div")
(print (send one-third :div one-half))



;;; 
#|(setf (symbol-function '+-org)(symbol-function '+))
(defun + (a b)
  (if (derivedp a rat)
      (send a :add b)
    (+-org a b)))

(print (+ one-third one-half))
|#
