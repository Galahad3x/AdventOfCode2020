inputs = [1826,1895,1427,1931,1651,1638,1507,1999,1886,1824,1902,1995,1945,1735,1823,1595,1936,1476,2010,1833,1932,1772,1791,1814,1783,1957,1901,1600,1502,1521,1812,1974,1880,1790,1672,1541,1807,426,1858,1699,1964,1996,1983,1498,1863,1976,1492,1930,1838,1941,1764,1929,1897,2009,1853,1753,1759,1860,1952,1988,1727,1751,1943,1830,1645,1907,1857,1714,1798,1944,1868,1630,959,2003,1987,1890,1962,1928,1872,1912,1709,1809,1650,1980,1737,1898,1817,1736,1991,1788,1776,1845,1854,1963,1554,1949,1576,1819,1960,699,1990,1757,1698,1596,304,1982,1477,1961,1636,1619,1946,1876,1592,1848,1707,1958,1874,1867,52,1881,1665,1463,1799,1979,677,1710,1869,1639,1787,1633,1956,1457,1581,2005,1782,1904,1910,62,1593,1695,1915,1922,1797,1715,1981,1925,1893,1562,1789,2008,1939,1669,1992,1652,117,1609,1686,1953,2007,599,1547,1959,1691,1520,1444,1641,887,1579,1778,1977,1768,1942,1713,1603,1926,1855,1655,1673,1887,1994,1839,1725,928,1771,1761,1971,1571,1806,1821,1624,1701,1436,1748,1921,1617,2004,1792,1732,1740,1831]


main = do
	putStrLn "Part 1: "
	putStrLn $ show part_1
	putStrLn "Part 2: "
	putStrLn $ show part_2
	
part_2 :: Int
part_2 = (part_2_res!!0) * (part_2_res!!1) * (part_2_res!!2)
	where part_2_res = part_2' inputs

part_2' :: [Int] -> [Int]
part_2' [] = [0, 0, 0]
--suma_res retorna una tupla amb els 2 sumants que falten, si retorna (0, _) vol dir que x no té cap altres 2 numeros amb qui sumar 2020
part_2' (x:xs) = if (fst suma_res) /= 0 then [x, fst suma_res, snd suma_res] else part_2' xs
	where suma_res = trobar_suma_3 x xs
	
-- mirar si x1 es un dels 3 sumants
trobar_suma_3 :: Int -> [Int] -> (Int, Int)
trobar_suma_3 _ [] = (0, 0)
-- res es el 3r sumant -> Fixant x1 i x si en trobo un altre es res
-- si res es 0 x1 + x no te cap numero que sumat doni 2020
trobar_suma_3 x1 (x:xs) = if res /= 0 then (x, res) else trobar_suma_3 x1 xs
	where res = trobar_suma_3' x1 x xs
	
trobar_suma_3' :: Int -> Int -> [Int] -> Int
trobar_suma_3' _ _ [] = 0
trobar_suma_3' x1 x2 (x:xs) = if x1 + x2 + x == 2020 then x else trobar_suma_3' x1 x2 xs

part_1 :: Int
part_1 = (fst part_1_res) * (snd part_1_res)
	where part_1_res = part_1' inputs
	
part_1' :: [Int] -> (Int, Int)
part_1' [] = (0, 0)
part_1' (x:xs) = if suma_res /= 0 then (x, suma_res) else part_1' xs
	where suma_res = trobar_suma_2 x xs
	
trobar_suma_2 :: Int -> [Int] -> Int
trobar_suma_2 _ [] = 0
trobar_suma_2 x1 (x:xs) = if x1 + x == 2020 then x else trobar_suma_2 x1 xs
