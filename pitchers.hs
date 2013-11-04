import qualified Data.Set as Set

-- solve [8,5,3] 4
-- solve [10,7,3] 5
--http://www.ccs.neu.edu/course/cs5010f13/problem-sets/ps07.html

data Pitcher = Pitcher { contents:: Int
                       , capacity:: Int
                       } deriving (Show, Eq, Ord)    


data Move = Move { src::Int
                 , tgt::Int} deriving(Show)

data Configuration = Configuration { pitchers :: [Pitcher]
                                   , moves :: [Move]} deriving (Show)
instance Eq Configuration where
    (Configuration p1 _) == (Configuration p2 _) = p1 == p2

instance Ord Configuration where
    compare (Configuration p1 _ ) (Configuration p2 _) = compare p1 p2
pitchersAfterMove :: [Pitcher] -> Move -> [Pitcher]
pitchersAfterMove pitchers move
                  |(src move) <(tgt move) = take (src move -1) pitchers ++ [Pitcher (src_contents - delta) src_capacity]
                                            ++ (drop (src move) $ take (tgt move - 1) $ pitchers)
                                            ++ [Pitcher (tgt_contents + delta) tgt_capacity] ++ (drop (tgt move) pitchers)
                  | otherwise =  take (tgt move -1) pitchers ++ [Pitcher (tgt_contents + delta) tgt_capacity]
                                            ++ (drop (tgt move) $ take (src move - 1) $ pitchers)
                                            ++ [Pitcher (src_contents - delta) src_capacity] ++ (drop (src move) pitchers)
                  where src_pitcher = pitchers !! (src move - 1)
                        tgt_pitcher = pitchers !! (tgt move - 1)
                        src_contents = contents src_pitcher
                        tgt_contents = contents tgt_pitcher
                        src_capacity = capacity src_pitcher
                        tgt_capacity = capacity tgt_pitcher
                        delta = min src_contents (tgt_capacity - tgt_contents)

pitchersFromList :: [Int] -> [Pitcher]
pitchersFromList (x:xs) = [Pitcher x x] ++ (map (Pitcher 0) xs) 

pitchersAfterMoves :: [Pitcher] -> [Move] -> [Pitcher]
pitchersAfterMoves pitchers moves = foldl pitchersAfterMove pitchers moves


configurationAfterMove :: Configuration -> Move -> Configuration
configurationAfterMove (Configuration pitchers moves) move =
    Configuration (pitchersAfterMove pitchers move) (moves++[move])

nextConfigurations :: Int -> Configuration -> Set.Set Configuration
nextConfigurations n configuration =
    Set.fromList $  map (configurationAfterMove configuration) [Move i j| i<-[1..n], j<-[1..n], i/=j]

successors :: Int -> Set.Set Configuration -> Set.Set Configuration
successors n configurations = foldl Set.union Set.empty $ map (nextConfigurations n) $  Set.toList configurations

pitchersReachedGoal :: [Pitcher] -> Int -> Bool
pitchersReachedGoal pitchers goal = any (== goal) $ map contents pitchers 

configurationReachedGoal :: Configuration -> Int -> Bool
configurationReachedGoal (Configuration pitchers _) goal = pitchersReachedGoal pitchers goal

solver :: Set.Set Configuration -> Set.Set Configuration -> Int -> Int -> Maybe [Move]
solver searched newest goal n 
       | (not $ Set.null answer) = Just (moves $ head $ Set.toList answer)
       | (Set.null candidates) = Nothing
       | otherwise = solver searchednew candidates goal n
       where answer = Set.filter (\x -> configurationReachedGoal x goal) newest
             searchednew = Set.union searched newest
             candidates  = Set.difference (successors n newest) searchednew 
solve :: [Int] -> Int -> Maybe [Move]
solve lst goal = solver Set.empty (Set.fromList [Configuration (pitchersFromList lst) []]) goal (length lst)
