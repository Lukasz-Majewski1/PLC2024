--create inpFunc
inpFunc a b = [a..b]

--Define applicatorFunc
applicatorFunc a b s = if s =='s' then sum (inpFunc a b) else sum (inpFunc a b) / (b - a + 1)

main = do
    let result = applicatorFunc 1 5 'a'
    putStrLn("sum = " ++ show(result))