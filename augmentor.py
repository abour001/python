import Augmentor

src_dir = ''
nb_img = int(1e1) # Number of images you want to generate

# Initializing Pipepline 
p = Augmentor.Pipeline(src_dir)

# Create transformations
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.rotate(probability=1, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.flip_left_right(probability=0.6)
p.flip_top_bottom(probability=0.5)
p.gaussian_distortion(probability=0.8, grid_width=10, grid_height=10, magnitude=10,
                      corner='bell', method='in', mex=0.5, mey=0.5, sdx=0.05, sdy=0.05)
p.scale(probability=0.7, scale_factor=2)
p.shear(probability=0.5, max_shear_left=10, max_shear_right=10)
p.skew(probability=1, magnitude=0.2)



# Generate samples
p.sample(nb_img)