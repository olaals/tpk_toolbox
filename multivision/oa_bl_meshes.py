import bpy
import random

def add_cuboid(name, size=(1,1,1), offset=(0,0,0), location=(0,0,0)):
    """
    Add a cuboid ("3D rectangle cube") with size = (x,y,z)
    Parameters:
    name: name of the object 
    size: (x,y,z) size of the object
    offset: (optional) offset the mesh from the position of the object
    location: set (x,y,z) location of the object

    Returns:
    Object with cuboid mesh linked

    Example:
    cuboid_obj = add_cuboid("MyCube", (1.0, 2.0, 0.5))
    """
    x = size[0]
    y = size[1]
    z = size[2]
    xo = offset[0]
    yo = offset[1]
    zo = offset[2]

    bottom_verts = [(-x/2+xo, -y/2+yo, -z/2+zo), (-x/2+xo, y/2+yo, -z/2+zo), (x/2+xo, y/2+yo, -z/2+zo), (x/2+xo, -y/2+yo, -z/2+zo)]
    top_verts = [(-x/2+xo, -y/2+yo, z/2+zo), (-x/2+xo, y/2+yo, z/2+zo), (x/2+xo, y/2+yo, z/2+zo), (x/2+xo, -y/2+yo, z/2+zo)]

    verts = bottom_verts + top_verts
    faces = [(0,1,2,3), (4,5,6,7), (0,1,5,4), (1,2,6,5), (2,3,7,6), (0,4,7,3)]
    edges = []

    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    mesh.from_pydata(verts,edges,faces)
    bpy.context.collection.objects.link(obj)
    return obj

def add_plane(name, size=(1,1), offset=(0,0,0), location=(0,0,0)):
    x = size[0]
    y = size[1]
    xo = offset[0]
    yo = offset[1]
    zo = offset[2]
    verts = [(-x/2+xo, -y/2+yo, zo), (-x/2+xo, y/2+yo, zo), (x/2+xo, y/2+yo, zo), (x/2+xo, -y/2+yo, zo)]
    faces = [(0,1,2,3)]
    edges = []
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name,mesh)
    obj.location = location
    mesh.from_pydata(verts,edges,faces)
    bpy.context.collection.objects.link(obj)
    return obj


def assign_random_orientation(object):
    object.rotation_euler = (random.uniform(0, 6.24), random.uniform(0,6.24), random.uniform(0,6.24))

def assign_random_location_with_limits(object, limits_min, limits_max):
    x = random.uniform(limits_min[0], limits_max[0])
    y = random.uniform(limits_min[1], limits_max[1])
    z = random.uniform(limits_min[2], limits_max[2])
    object.location = (x,y,z)

def assign_random_scaling_with_limits(object, limits_min, limits_max):
    x = random.uniform(limits_min[0], limits_max[0])
    y = random.uniform(limits_min[1], limits_max[1])
    z = random.uniform(limits_min[2], limits_max[2])
    object.scale[0] *= x
    object.scale[1] *= y
    object.scale[2] *= z