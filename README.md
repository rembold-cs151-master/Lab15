# Lab15

This lab is about generating a comparison table of the run-time of different sorting methods on arrays of varying length.

The table might look something like below, though your numbers will be different:
```
         N  Selection      Merge     Bubble
---------- ---------- ---------- ----------
        10    0.00001    0.00001    0.00001
        20    0.00001    0.00002    0.00002
        40    0.00004    0.00005    0.00007
        80    0.00015    0.00011    0.00030
       160    0.00056    0.00024    0.00111
       320    0.00260    0.00113    0.00616
       640    0.01113    0.00109    0.02317
      1280    0.04200    0.00226    0.09539
      2560    0.17151    0.00504    0.39356
      5120    0.67029    0.01090    1.64599
     10240    2.63010    0.02198    6.42580
```

No autotests for this lab, so just make sure your table looks reasonable and that you have addressed the last question in a comment at the bottom of your code.
