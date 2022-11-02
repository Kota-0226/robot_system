(setq s1
      (make-gdome (make-gdome (make-gdome (make-icosahedron 50)))))
(send s1 :set-color :yellow)
(send s1 :locate #f(100 200 0))

(setq s2
      (make-gdome (make-gdome (make-gdome (make-icosahedron 100)))))
(send s2 :set-color :blue)

(send s2 :assoc s1)

(make-irtviewer)
(objects (list s1 s2))

(dotimes (i 100)
  (send s2 :rotate (deg2rad 2) :z)
  (send *irtviewer* :draw-objects) ;; 画面を再描画する
  (x::window-main-one)) ;; GUI のイベント処理を行う
