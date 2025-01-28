empty_set={}
print(empty_set)
vehicles={'boat','car','plane','jet','train','bike','submarine'}
on_road={'car','bike','auto','bus'}
on_water={'boat','submarine'}
on_air={'plane','jet'}
on_tracks={'train'}
print(vehicles|on_road)
print(vehicles.union(on_road))
print(vehicles & on_water)
print(vehicles.intersection(on_water))