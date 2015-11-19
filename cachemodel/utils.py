from hashlib import md5


def generate_cache_key(prefix, *args, **kwargs):
    arg_str = ":".join(str(a) for a in args)
    kwarg_str = ":".join("%s=%s" % (str(k), str(v)) for k, v in kwargs.items())
    key_str = "%s::%s" % (arg_str, kwarg_str)
    argkwarg_str = md5(bytes(key_str, "ASCII")).hexdigest()
    if not isinstance(prefix, basestring):
        prefix = "_".join(str(a) for a in prefix)
    return "%s__%s" % (prefix, argkwarg_str)
